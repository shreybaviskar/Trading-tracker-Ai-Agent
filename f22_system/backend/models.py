from sqlalchemy import Column, Integer, String
from database import Base

class MarketContext(Base):
    __tablename__ = "market_context"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class LevelInput(Base):
    __tablename__ = "level_input"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, index=True)

class DecisionRule(Base):
    __tablename__ = "decision_rule"
    id = Column(Integer, primary_key=True, index=True)
    rule = Column(String, index=True)

class ChartAnalysis(Base):
    __tablename__ = "chart_analysis"
    id = Column(Integer, primary_key=True, index=True)
    analysis = Column(String, index=True)

class TradeValidation(Base):
    __tablename__ = "trade_validation"
    id = Column(Integer, primary_key=True, index=True)
    validation = Column(String, index=True)

class JournalEntry(Base):
    __tablename__ = "journal_entry"
    id = Column(Integer, primary_key=True, index=True)
    entry = Column(String, index=True)

class ReportRequest(Base):
    __tablename__ = "report_request"
    id = Column(Integer, primary_key=True, index=True)
    request = Column(String, index=True)
