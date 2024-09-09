import json
from talib import abstract
import talib
from fastapi import FastAPI, Request
import pandas as pd
from ta import add_all_ta_features

app = FastAPI()


@app.get("/")
def test_ground():
    return "test mic! test mic!"


async def get_result(candlestick, positive, negative,request):
            # get the OHLC from MT5
            candles = await request.body()
            # turn the bytes to string
            candles=candles.decode('utf8').replace("'", '"')
            # turn the string to json
            candles = json.loads(candles)
            # create a df
            df = pd.DataFrame(candles)
            # Three inside up or down 
            df[str(candlestick)] = getattr(abstract, str(candlestick))(df)
            # get the 
            last_element = df[str(candlestick)].iloc[-1]
            if 0 < last_element <= 100 and positive:
                return "up"
            elif  0 > last_element >= -100 and negative:
                return "down"
            else:
                return "none"
    
@app.post("/two_crows")
async def two_crows(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL2CROWS.c#L222
    Integer is negative (-1 to -100): advance block is always bearish;
    """
    return await get_result("CDL2CROWS", False, True,request)


@app.post("/three_black_crows")
async def three_black_crows(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3BLACKCROWS.c#L226
    Integer is negative (-1 to -100): three black crows is always bearish; 

    """
    return await get_result("CDL3BLACKCROWS", False, True,request)
    

@app.post("/three_inside_up_down")
async def three_inside_up_down(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3INSIDE.c#L222
    Integer is positive (1 to 100) for the three inside up or negative (-1 to -100) for the three inside down; 
    """
    return await get_result("CDL3INSIDE", True, True,request)
    

@app.post("/three_line_strike")
async def three_line_strike(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3LINESTRIKE.c#L224C10-L224C68
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
    """
    return await get_result("CDL3LINESTRIKE", True, True,request)
    

@app.post("/three_outside_up_or_down")
async def three_outside_up_or_down(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3OUTSIDE.c#L211C10-L211C117
    Integer is positive (1 to 100) for the three outside up or negative (-1 to -100) for the three outside down
    """
    return await get_result("CDL3OUTSIDE", True, True,request)


@app.post("/three_stars_in_the_south")
async def three_stars_in_the_south(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3STARSINSOUTH.c#L249
    Integer is positive (1 to 100): 3 stars in the south is always bullish;
    """
    return await get_result("CDL3STARSINSOUTH", True, False,request)    
    
    
@app.post("/three_advancing_white_soldiers")
async def three_advancing_white_soldiers(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3WHITESOLDIERS.c#L260
    Integer is positive (1 to 100): advancing 3 white soldiers is always bullish;
    """
    return await get_result("CDL3WHITESOLDIERS", True, False,request)


    
@app.post("/abandoned_baby")
async def abandoned_baby(request: Request):
    """
    Link to the core:
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLABANDONEDBABY.c#L265
    Integer is positive (1 to 100) when it's an abandoned baby bottom or negative (-1 to -100) when it's an abandoned baby top;     
    """
    return await get_result("CDLABANDONEDBABY", True, True,request)

    
@app.post("/advanced_blocks")
async def advanced_blocks(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLADVANCEBLOCK.c#L260
    Integer is negative (-1 to -100): two crows is always bearish; 
    """
    return await get_result("CDLADVANCEBLOCK", False, True,request)


@app.post("/belt_hold")
async def belt_hold(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLBELTHOLD.c#L260
    Integer is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
    """
    return await get_result("CDLBELTHOLD", False, True,request)


    

    

