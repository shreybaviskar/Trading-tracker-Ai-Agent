from pydantic import BaseModel

class MarketContext(BaseModel):
    market_type: str
    volatility_expectation: float
    breakout_risk: bool
    sentiment: str
    htf_support_resistance_map: dict
    high_impact_news: str

class LevelInput(BaseModel):
    support: float
    resistance: float
    liquidity_zone: str
    vwap_reference: str
    session_level: str
    watchlist_zone: str

class DecisionRule(BaseModel):
    condition: str
    action: str

class ChartAnalysis(BaseModel):
    trend: str
    range: bool
    liquidity_sweep: bool
    break_retest: bool
    reversal: bool
    vwap_state: str
    structure_clarity: bool

class TradeValidation(BaseModel):
    price_near_level: bool
    liquidity_sweep: bool
    timing_window: str
    risk_reward_ratio: float

class JournalEntry(BaseModel):
    entry_time: datetime.datetime
    trade_type: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward_ratio: float

class ReportRequest(BaseModel):
    report_type: str
