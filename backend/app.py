from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io

from database import engine, SessionLocal
from models import Base, QCReport
from collections import Counter

app = FastAPI()

#allows react frontend to access backend api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#creates database tables based on models if they don't exist
Base.metadata.create_all(bind=engine)

COLUMN_MAPPING = {
    "Date": "date",
    "Product": "product",
    "Employee": "employee",
    "Department": "department",
    "Defect Type": "defect_type",
    "Description": "description",
    "Severity": "severity",

    # Possible Epicor-style names
    "PartNum": "product",
    "OperatorID": "employee",
    "IssueText": "description",
    "Area": "department",
    "SeverityLevel": "severity"
}

#simple endpoint to test if backend is running
@app.get("/")
def home():
    return {"message": "QC Insight AI Backend Running"}

#uplaods csv or excel file, parses it, and stores the data in the database. Returns a summary of the upload results
@app.post("/upload-preview")
async def upload_preview(file: UploadFile = File(...)):
    #reads the uploaded file into memory
    contents = await file.read()

    #if the file is CSV read with pandas
    if file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(contents))
    #if the file is Excel read with pandas
    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(io.BytesIO(contents))
    #reject unsupported file types
    else:
        return {"error": "Only CSV and Excel .xlsx files are supported"}
    
    #replace empty cells with empty strings
    df = df.fillna("")
    
    #rename columns to match the database model
    df = df.rename(columns=COLUMN_MAPPING)

    #open database section
    db = SessionLocal()

    #loop through every row in the uploaded file
    for _, row in df.iterrows():
        #create a QCReport object from the row data
        report = QCReport(
            date=str(row.get("date", "")),
            product=str(row.get("product", "")),
            employee=str(row.get("employee", "")),
            department=str(row.get("department", "")),
            defect_type=str(row.get("defect_type", "")),
            description=str(row.get("description", "")),
            severity=str(row.get("severity", ""))
        )

        #add re[port to the database session
        db.add(report)
    #save all reports to the database and close the session
    db.commit()
    db.close()

    return {
        "message": "Reports uploaded successfully",
        "rows_imported": len(df)
    }

#returns all saved QC Reports fro the DB
@app.get("/reports")
def get_reports():

    db = SessionLocal()

    reports = db.query(QCReport).all()

    db.close()

    return reports

#returns analytics sumamry data for the frontend
@app.get("/analytics/summary")
def analytics_summary():

    db = SessionLocal()

    reports = db.query(QCReport).all()

    db.close()

    #count total reports
    total_reports = len(reports)

    #count reports by catagory
    products = Counter(report.product for report in reports)
    employees = Counter(report.employee for report in reports)
    severities = Counter(report.severity for report in reports)
    defect_types = Counter(report.defect_type for report in reports)

    #return data inm JSON format for frontend dashboard
    return {
        "total_reports": total_reports,

        "top_products": dict(products),

        "top_employees": dict(employees),

        "severity_breakdown": dict(severities),

        "defect_types": dict(defect_types)
    }