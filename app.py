import json
from talib import abstract
from fastapi import FastAPI, Request
import pandas as pd

app = FastAPI()




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
  
 
@app.get("/")
def test_ground():
    return "test mic! test mic!"

   
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
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLADVANCEBLOCK.c#L271
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
    return await get_result("CDLBELTHOLD", True, True,request)


  
@app.post("/breakaway")
async def breakaway(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLBREAKAWAY.c#L223
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
    """
    return await get_result("CDLBREAKAWAY", True, True,request)

  
@app.post("/closing_marubozu")
async def closing_marubozu(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLCLOSINGMARUBOZU.c#L235
    Integer is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
    """
    return await get_result("CDLCLOSINGMARUBOZU", True, True,request)


@app.post("/conceal_baby_swallow")
async def conceal_baby_swallow(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLCONCEALBABYSWALL.c#L230
    Integer is positive (1 to 100): concealing baby swallow is always bullish;
    """
    return await get_result("CDLCONCEALBABYSWALL", True, False,request)



@app.post("/counterattack")
async def counterattack(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLCOUNTERATTACK.c#L235
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
    """
    return await get_result("CDLCOUNTERATTACK", True, True,request)



@app.post("/dark_cloud_cover")
async def dark_cloud_cover(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLDARKCLOUDCOVER.c#L245
    Integer is negative (-1 to -100): dark cloud cover is always bearish
    """
    return await get_result("CDLDARKCLOUDCOVER", False, True,request)


@app.post("/doji")
async def doji(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLDOJI.c#L226
    Integer is always positive (1 to 100) but this does not mean it is bullish: doji shows uncertainty and it is

    """
    return await get_result("CDLDOJI", True, False,request)

@app.post("/doji_star")
async def doji_star(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLDOJISTAR.c#L230
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
    """
    return await get_result("CDLDOJISTAR", True, True,request)


@app.post("/dragonfly_doji")
async def dragonfly_doji(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLDRAGONFLYDOJI.c#L236
    Integer is always positive (1 to 100) but this does not mean it is bullish: 
    """
    return await get_result("CDLDRAGONFLYDOJI", True, False,request)

@app.post("/engulfing_pattern")
async def engulfing_pattern(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLENGULFING.c#L212
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
    - 100 is returned when the second candle's real body begins before and ends after the first candle's real body
    - 80 is returned when the two real bodies match on one end (Greg Morris contemplate this case in his book "Candlestick charting explained")
    """
    return await get_result("CDLENGULFING", True, True,request)


@app.post("/evening_doji_star")
async def evening_doji_star(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLEVENINGDOJISTAR.c#L267
    Integer is negative (-1 to -100): evening star is always bearish; 
    """
    return await get_result("CDLEVENINGDOJISTAR", False, True,request)


@app.post("/evening_star")
async def evening_star(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLEVENINGSTAR.c#L260
    Integer is negative (-1 to -100): evening star is always bearish; 
    """
    return await get_result("CDLEVENINGSTAR", False, True,request)



@app.post("/up_or_down_gap_side_by_side_white_lines")
async def up_or_down_gap_side_by_side_white_lines(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLGAPSIDESIDEWHITE.c#L230
    Integer is positive (1 to 100) or negative (-1 to -100)
    """
    return await get_result("CDLGAPSIDESIDEWHITE", True, True,request)

@app.post("/gravestone_doji")
async def gravestone_doji(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLGRAVESTONEDOJI.c#L228
    Integer is always positive (1 to 100) but this does not mean it is bullish 
    """
    return await get_result("CDLGRAVESTONEDOJI", True, False,request)



@app.post("/hammer")
async def hammer(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHAMMER.c#L246
    Integer is positive (1 to 100): hammer is always bullish;
    """
    return await get_result("CDLHAMMER", True, False,request)

@app.post("/hanging_man")
async def hanging_man(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHANGINGMAN.c#L246
    Integer is negative (-1 to -100): hanging man is always bearish;
    """
    return await get_result("CDLHANGINGMAN", False, True,request)

@app.post("/harami_pattern")
async def harami_pattern(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHARAMI.c#L233
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
     - 100 is returned when the first candle's real body begins before and ends after the second candle's real body
     - 80 is returned when the two real bodies match on one end (Greg Morris contemplate this case in his book "Candlestick charting explained"
    """
    return await get_result("CDLHARAMI", True, True,request)


@app.post("/harami_cross_pattern")
async def harami_cross_pattern(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHARAMICROSS.c#L233
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
    """
    return await get_result("CDLHARAMICROSS", True, True,request)


@app.post("/high_wave_candle")
async def high_wave_candle(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHIGHWAVE.c#L226
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
    """
    return await get_result("CDLHIGHWAVE", True, True,request)