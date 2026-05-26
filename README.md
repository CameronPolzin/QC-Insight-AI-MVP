# QC Insight AI

## AI-Powered Quality Analytics Platform for Manufacturing Operations

---

# Overview

QC Insight AI is a quality analytics platform designed to help manufacturing and quality assurance teams at Global Power Components transform raw discrepancy and nonconformance data into actionable operational insight.

The system is designed to integrate with the company’s existing workflows and ERP infrastructure, including Epicor ERP, to centralize quality data, analyze manufacturing discrepancies, and provide real-time analytics for process improvement and decision making.

The long-term vision is to create an intelligent quality platform capable of:

- Automated discrepancy analysis
- Trend detection
- Root cause insight generation
- Predictive quality analytics
- ERP-integrated manufacturing intelligence
- AI-assisted reporting and summarization
- Handwritten discrepancy processing
- Natural-language AI querying of QC data

---

# Problem Statement

Manufacturing and QC departments generate large amounts of discrepancy and nonconformance data every day. However, much of this information is:

- Stored across disconnected spreadsheets and reports
- Difficult to analyze at scale
- Time consuming to review manually
- Reactive rather than proactive
- Underutilized for trend analysis and process improvement
- Archived in handwritten paper records that are difficult to search or analyze

Although Epicor ERP already stores important operational and quality data, there is an opportunity to build an analytics-focused layer that continuously processes discrepancy information and transforms it into actionable intelligence for quality, engineering, and management teams.

This project aims to create a centralized analytics platform capable of continuously analyzing QC data and providing meaningful operational insight.

---

# Current MVP Features

## Frontend Dashboard

- React dashboard interface
- Live analytics pulled from FastAPI backend
- Bar charts for defect types and severity breakdown
- Product filtering
- Ascending/descending sorting
- Frontend Excel/CSV upload
- Dashboard refresh after upload

## Data Import

- Upload Excel (.xlsx) discrepancy reports
- Upload CSV discrepancy reports
- Parse uploaded QC data using Pandas
- Normalize varying report formats into a standard internal structure

## Flexible Column Mapping

The system supports varying export formats by automatically mapping uploaded column names to standardized internal fields.

### Example

| Uploaded Column | Internal Field |
|---|---|
| PartNum | product |
| OperatorID | employee |
| IssueText | description |
| SeverityLevel | severity |

This allows the platform to support:

- Epicor exports
- Existing QC spreadsheets
- Other ERP systems
- Future integrations

---

## Database Storage

- Stores imported discrepancy reports in a centralized database
- Structured QC report model
- Persistent historical discrepancy tracking

---

## Analytics API

The current analytics system provides:

- Total discrepancy counts
- Defects by product
- Defects by employee/operator
- Severity breakdowns
- Most common defect types

---

# Example Workflow

```text
Epicor Export / QC Spreadsheet / Discrepancy Data
                        ↓
                   Upload File
                        ↓
              Data Normalization
                        ↓
              Database Persistence
                        ↓
                Analytics Engine
                        ↓
             Dashboard / AI Insights
```

---

# Example Use Cases

## Quality Control Teams

- Track recurring production defects
- Monitor defect trends over time
- Identify bottlenecks in production processes
- Compare quality performance between departments or production lines

---

## Supervisors and Management

- Review quality metrics quickly
- Identify high-risk products or operations
- Generate operational summaries
- Support continuous improvement initiatives

---

## Engineering and Manufacturing Teams

- Analyze recurring root causes
- Detect process drift or recurring manufacturing issues
- Compare defect frequency across product families
- Improve operational efficiency using historical quality data

---

# Future AI Features

Potential future AI functionality includes:

- Automatic defect categorization
- AI-generated discrepancy summaries
- Root cause suggestion engine
- Trend prediction
- Supplier quality analysis
- Predictive maintenance indicators
- Natural-language querying
- AI-generated operational recommendations

### Example Queries

> “Which products had the highest increase in discrepancies this month?”

> “What are the most common weld-related discrepancies?”

> “Which departments generate the most high-severity discrepancies?”

> “Summarize recurring quality issues from last quarter.”

---

# Handwritten Discrepancy Processing (Planned)

A long-term goal of the platform is to support both digital and paper-based quality records currently used throughout manufacturing and QC processes.

Future versions will allow users to:

- Upload scanned handwritten discrepancy reports
- Upload photographed paper discrepancy forms
- Process reports using OCR and handwriting recognition
- Extract structured QC data using AI
- Validate extracted data through a human review step
- Store processed records for analytics and reporting

### Example Workflow

```text
Handwritten QC Report
            ↓
       Scan/Image Upload
            ↓
 OCR / Handwriting Recognition
            ↓
      AI Data Extraction
            ↓
        Human Validation
            ↓
       Database Storage
            ↓
    Analytics & AI Insights
```

---

# Integrated AI Assistant (Planned)

Future versions of the platform will include an integrated AI assistant capable of answering natural-language questions about stored QC and manufacturing data.

Instead of manually filtering spreadsheets or reports, users could ask:

```text
“What product has the most discrepancies this month?”

“Which operators are tied to recurring weld defects?”

“What are the most common root causes?”

“Show recurring issues for Product A12.”

“Summarize high-severity discrepancies from last week.”
```

The AI assistant would query the database directly and generate answers grounded in the organization’s actual quality records.

---

# Technical Architecture

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pandas

---

## Database

- SQLite (current MVP)
- PostgreSQL (planned)

---

## Frontend

- React
- Recharts
- Tailwind CSS

---

## Future Integrations

- Epicor ERP API integration
- Automated ERP synchronization
- Power BI integration
- OCR and handwriting recognition
- AI/NLP services

---

# Current Project Status

## Completed

- Backend API setup
- File upload system
- Excel and CSV import
- Dynamic column normalization
- Database persistence
- Analytics endpoints
- Dashboard frontend
- Advanced filtering/search
- Data visualization

---

## In Progress

- Date range filtering
- Trend charts over time
- Improved dashboard styling

---

## Planned Features

- Date range filtering
- Defects-over-time trend analysis
- Exportable reports
- AI-powered analytics
- Predictive trend analysis
- Automated reporting
- User authentication
- Role-based access
- ERP live synchronization
- Real-time alerting
- OCR integration
- Handwritten report processing
- Natural-language AI assistant

---

# Why This Project Matters

This project combines:

- Manufacturing operations
- Data engineering
- Software development
- Analytics
- Artificial intelligence
- Process improvement

The goal is not only to digitize QC reporting, but to transform manufacturing quality data into a proactive decision-making tool.

By centralizing and analyzing quality data, the platform can help:

- Detect trends earlier
- Reduce recurring defects
- Improve operational visibility
- Increase manufacturing efficiency
- Support data-driven decision making

---

# Local Development Setup

## Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload

## Frontend

cd frontend
npm install
npm run dev

--- 

# Author

Cameron Polzin  
Computer Science Student
