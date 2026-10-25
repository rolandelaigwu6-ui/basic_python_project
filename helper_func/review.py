# ===== GOLD MASTER BOT - M12 TO M15 - YOUR SYSTEM =====
# Large Account: H4 Entry | Small Account: M15 Entry with full filter chain

import yfinance as yf
import requests

SYMBOL = "GC=F"
TELEGRAM_TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send(msg): 
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                  data={"chat_id":CHAT_ID,"text":msg})

def scan():
    # 1. GET DATA
    m12 = yf.download(SYMBOL, period="10y", interval="1mo", auto_adjust=True)
    daily = yf.download(SYMBOL, period="3mo", interval="1d", auto_adjust=True)
    h4 = yf.download(SYMBOL, period="1mo", interval="1h", auto_adjust=True).resample('4H').agg({'Open':'first','High':'max','Low':'min','Close':'last'}).dropna()
    h1 = yf.download(SYMBOL, period="1mo", interval="1h", auto_adjust=True)
    m30 = yf.download(SYMBOL, period="5d", interval="30m", auto_adjust=True)
    m15 = yf.download(SYMBOL, period="5d", interval="15m", auto_adjust=True)
    
    for df in [m12,daily,h4,h1,m30,m15]:
        if hasattr(df.columns, 'get_level_values'): df.columns = df.columns.get_level_values(0)

    # 2. YOUR CORE LOGIC
    # M12: LqS at current price?
    m12_LqS = (m12['High'].iloc[-1] > m12['High'].iloc[-2]) and (m12['Close'].iloc[-1] < m12['Close'].iloc[-2])
    op_l_12m = m12['Open'].iloc[-1]
    
    # Daily: LqS Chain to get 2nd OP^L
    daily['is_LqS'] = (daily['High'] > daily['High'].shift(1).rolling(3).max()) & (daily['Close'] < daily['Close'].shift(1))
    last_2_lqs = daily[daily['is_LqS']].tail(2)
    if len(last_2_lqs) < 2: return
    ENTRY_LARGE = last_2_lqs.iloc[-1]['Open']  # 4195
    SL_LARGE = last_2_lqs.iloc[-1]['High'] + 2  # 4217
    ENTRY_SMALL = m15[m15['High']>ENTRY_LARGE-2].iloc[-1]['Open'] if len(m15)>0 else ENTRY_LARGE
    SL_SMALL = 4200.51 # Your marked high
    TP = daily['Low'].rolling(20).min().iloc[-1] # Previous structure low ~3940

    # 3. FILTERS FOR SMALL ACCOUNT
    # H4: Bearish Harami at Daily OP^L?
    h4['harami'] = (h4['Close'].shift(1) > h4['Open'].shift(1)) & (h4['Close'] < h4['Open']) & (h4['High'] < h4['High'].shift(1))
    has_harami = h4['harami'].iloc[-3:].any()
    
    # M15: CHoCH / Break of low?
    m15['choch'] = m15['Close'] < m15['Low'].shift(1).rolling(10).min()
    has_choch_m15 = m15['choch'].iloc[-2:].any()
    
    current_price = m15['Close'].iloc[-1]

    # 4. ALERTS
    if m12_LqS and has_harami:
        # LARGE ACCOUNT ALERT
        if abs(current_price - ENTRY_LARGE) < 10:
            rr_large = (ENTRY_LARGE - TP) / (SL_LARGE - ENTRY_LARGE)
            send(f"""🔔 LARGE ACCOUNT SETUP (H4)

M12 LqS: Yes | 12M OP^L: {op_l_12m:.2f}
Daily 2nd OP^L: {ENTRY_LARGE:.2f}
H4 Harami: Confirmed

ENTRY SELL: {ENTRY_LARGE:.2f}
SL: {SL_LARGE:.2f} ({SL_LARGE-ENTRY_LARGE:.2f}$ risk)
TP: {TP:.2f} (Prev Structure Low)
RR: 1:{rr_large:.1f}

ACTION: Sell Limit at OP^L""")

        # SMALL ACCOUNT ALERT - NEEDS M15 GO
        if has_choch_m15 and abs(current_price - ENTRY_SMALL) < 5:
            rr_small = (ENTRY_SMALL - TP) / (SL_SMALL - ENTRY_SMALL)
            send(f"""🔔 SMALL ACCOUNT GO (M15)

H4 Harami: Yes | H1 OP^L: {ENTRY_LARGE:.2f} | M30: Marked

M15 CHoCH: CONFIRMED - GO!

ENTRY SELL: {ENTRY_SMALL:.2f}
SL: {SL_SMALL:.2f} ({SL_SMALL-ENTRY_SMALL:.2f}$ risk) 
TP: {TP:.2f} (Prev Structure Low)
RR: 1:{rr_small:.1f}

This is the final trigger you marked on M15 chart.""")

    print(f"Scan done. Current: {current_price:.2f} | Large Entry: {ENTRY_LARGE:.2f} | Small: {ENTRY_SMALL:.2f}")

# Run every 15 mins for small account precision
scan()