from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

from database import engine, SessionLocal
from models import Base, QCReport
from collections import Counter

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "QC Insight AI Backend Running"}

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

@app.post("/upload-preview")
async def upload_preview(file: UploadFile = File(...)):
    contents = await file.read()

    if file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(contents))
    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(io.BytesIO(contents))
    else:
        return {"error": "Only CSV and Excel .xlsx files are supported"}

    df = df.fillna("")

    df = df.rename(columns=COLUMN_MAPPING)

    db = SessionLocal()

    for _, row in df.iterrows():
        report = QCReport(
            date=str(row.get("date", "")),
            product=str(row.get("product", "")),
            employee=str(row.get("employee", "")),
            department=str(row.get("department", "")),
            defect_type=str(row.get("defect_type", "")),
            description=str(row.get("description", "")),
            severity=str(row.get("severity", ""))
        )

        db.add(report)

    db.commit()
    db.close()

    return {
        "message": "Reports uploaded successfully",
        "rows_imported": len(df)
    }


@app.get("/reports")
def get_reports():

    db = SessionLocal()

    reports = db.query(QCReport).all()

    db.close()

    return reports


@app.get("/analytics/summary")
def analytics_summary():

    db = SessionLocal()

    reports = db.query(QCReport).all()

    db.close()

    total_reports = len(reports)

    products = Counter(report.product for report in reports)
    employees = Counter(report.employee for report in reports)
    severities = Counter(report.severity for report in reports)
    defect_types = Counter(report.defect_type for report in reports)

    return {
        "total_reports": total_reports,

        "top_products": dict(products),

        "top_employees": dict(employees),

        "severity_breakdown": dict(severities),

        "defect_types": dict(defect_types)
    }