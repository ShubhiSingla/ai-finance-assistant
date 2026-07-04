import yfinance as yf
from yfinance.exceptions import YFRateLimitError
from langchain_core.tools import tool


def resolve_ticker(query: str) -> tuple:
    """Convert company name to ticker symbol if needed.
    Returns (ticker, is_valid) tuple.
    """
    query = query.strip().upper()
    
    # Try the query as-is first
    try:
        ticker_obj = yf.Ticker(query)
        info = ticker_obj.info
        
        # Check multiple fields to verify it's valid
        if info and (info.get("currentPrice") or info.get("regularMarketPrice")):
            return query, True
    except:
        pass
    
    # Try common exchange suffixes for Indian stocks
    if not '.' in query:
        for suffix in ['.NS', '.BO']:
            try:
                test_ticker = query + suffix
                ticker_obj = yf.Ticker(test_ticker)
                info = ticker_obj.info
                
                if info and (info.get("currentPrice") or info.get("regularMarketPrice")):
                    return test_ticker, True
            except:
                continue
    
    return query, False


@tool
def get_stock_price(ticker: str) -> dict:
    """
    Fetch the latest stock price and basic company information.
    Supports US stocks (e.g., AAPL) and Indian stocks (e.g., RELIANCE.NS or RELIANCE.BO).
    """
    try:
        # Resolve and validate ticker
        resolved_ticker, is_valid = resolve_ticker(ticker)
        
        if not is_valid:
            return {
                "status": "error",
                "message": f"Could not find stock information for '{ticker}'. Please verify the ticker symbol. For Indian stocks, try adding .NS (NSE) or .BO (BSE) suffix."
            }
        
        info = yf.Ticker(resolved_ticker).info
        
        # Try multiple price fields
        price = info.get("currentPrice") or info.get("regularMarketPrice")
        
        if not price:
            return {
                "status": "error",
                "message": f"Could not retrieve price for '{ticker}'. The stock might be delisted or unavailable."
            }

        return {
            "status": "success",
            "ticker": resolved_ticker.upper(),
            "company": info.get("shortName") or info.get("longName") or resolved_ticker,
            "current_price": price,
            "currency": info.get("currency") or "USD"
        }

    except YFRateLimitError:
        return {
            "status": "error",
            "message": (
                "Yahoo Finance is temporarily rate limiting requests. "
                "Please try again in a few minutes."
            )
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Unable to fetch stock data: {str(e)}"
        }