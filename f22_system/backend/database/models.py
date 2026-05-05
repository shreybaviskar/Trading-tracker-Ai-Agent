from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from database.base import Base

Base = declarative_base()

class MarketContext(Base):
    __tablename__ = "market_context"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class LevelInput(Base):
    __tablename__ = "level_input"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class DecisionRule(Base):
    __tablename__ = "decision_rule"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ChartAnalysis(Base):
    __tablename__ = "chart_analysis"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class TradeValidation(Base):
    __tablename__ = "trade_validation"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class JournalEntry(Base):
    __tablename__ = "journal_entry"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ReportRequest(Base):
    __tablename__ = "report_request"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
