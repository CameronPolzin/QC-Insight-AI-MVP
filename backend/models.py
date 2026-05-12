from sqlalchemy import Column, Integer, String
from database import Base

class QCReport(Base):
    __tablename__ = "qc_reports"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(String)
    product = Column(String)
    employee = Column(String)
    department = Column(String)
    defect_type = Column(String)
    description = Column(String)
    severity = Column(String)