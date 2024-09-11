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

@app.post("/hikkake")
async def hikkake(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHIKKAKE.c#L239
    Integer[confirmationbar] is equal to 100 + the bullish hikkake result or -100 - the bearish hikkake result
    Note: if confirmation and a new hikkake come at the same bar, only the new hikkake is reported (the new hikkake 
    overwrites the confirmation of the old hikkake)    
    """
    return await get_result("CDLHIKKAKE", True, True,request)


@app.post("/modified_hikkake")
async def modified_hikkake(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHIKKAKEMOD.c#L256
    Integer[hikkake bar] is positive (1 to 100) or negative (-1 to -100) meaning bullish or bearish hikkake   
    """
    return await get_result("CDLHIKKAKEMOD", True, True,request)


@app.post("/modified_hikkake")
async def modified_hikkake(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHIKKAKEMOD.c#L256
    Integer[hikkake bar] is positive (1 to 100) or negative (-1 to -100) meaning bullish or bearish hikkake   
    """
    return await get_result("CDLHIKKAKEMOD", True, True,request)


@app.post("/homing_pigeon")
async def homing_pigeon(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLHOMINGPIGEON.c#L231
    Integer is positive (1 to 100): homing pigeon is always bullish; 
    """
    return await get_result("CDLHOMINGPIGEON", True, False,request)


@app.post("/identical_three_crows")
async def identical_three_crows(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLIDENTICAL3CROWS.c#L242
    Integer is negative (-1 to -100): identical three crows is always bearish; 
    """
    return await get_result("CDLIDENTICAL3CROWS", False, True,request)

@app.post("/in_neck")
async def in_neck(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLINNECK.c#L232
    Integer is negative (-1 to -100): in-neck is always bearish
    """
    return await get_result("CDLINNECK", False, True,request)

@app.post("/inverted_hammer")
async def inverted_hammer(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLINVERTEDHAMMER.c#L241
    Integer is positive (1 to 100): inverted hammer is always bullish;
    """
    return await get_result("CDLINVERTEDHAMMER", True, False,request)


@app.post("/kicking")
async def kicking(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLKICKING.c#L234
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish
    """
    return await get_result("CDLKICKING", True, True,request)


@app.post("/kicking_by_length")
async def kicking_by_length(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLKICKINGBYLENGTH.c#L234
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish
    """
    return await get_result("CDLKICKINGBYLENGTH", True, True,request)


@app.post("/ladder_bottom")
async def ladder_bottom(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLLADDERBOTTOM.c#L221
    Integer is positive (1 to 100): ladder bottom is always bullish; 
    """
    return await get_result("CDLLADDERBOTTOM", True, True,request)


@app.post("/longlegged_doji")
async def longlegged_doji(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLLONGLEGGEDDOJI.c#L227
    Integer is always positive (1 to 100) but this does not mean it is bullish: long legged doji shows uncertainty
    """
    return await get_result("CDLLONGLEGGEDDOJI", True, False,request)


@app.post("/long_line_candle")
async def long_line_candle(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLLONGLINE.c#L226
    Integer is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
    """
    return await get_result("CDLLONGLINE", True, True,request)


@app.post("/marubozu")
async def marubozu(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLMARUBOZU.c#L226
    Integer is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
    """
    return await get_result("CDLMARUBOZU", True, True,request)

@app.post("/matching_low")
async def matching_low(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLMATCHINGLOW.c#L220
    Integer is always positive (1 to 100): matching low is always bullish;
    """
    return await get_result("CDLMATCHINGLOW", True, False,request)


@app.post("/mat_hold")
async def mat_hold(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLMATHOLD.c#L262
    Integer is positive (1 to 100): mat hold is always bullish
    """
    return await get_result("CDLMATHOLD", True, False,request)

@app.post("/morning_doji_star")
async def morning_doji_star(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLMORNINGDOJISTAR.c#L262
    Integer is positive (1 to 100): morning doji star is always bullish;
    """
    return await get_result("CDLMORNINGDOJISTAR", True, False,request)


@app.post("/morning_star")
async def morning_star(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLMORNINGSTAR.c#L255
    Integer is positive (1 to 100): morning star is always bullish; 
    """
    return await get_result("CDLMORNINGSTAR", True, False,request)


@app.post("/on_neck")
async def on_neck(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLONNECK.c#L228
    Integer is negative (-1 to -100): on-neck is always bearish
    """
    return await get_result("CDLONNECK", False, True,request)


@app.post("/piercing_pattern")
async def piercing_pattern(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLPIERCING.c#L223
    Integer is positive (1 to 100): piercing pattern is always bullish
    """
    return await get_result("CDLPIERCING", True, False,request)



@app.post("/rickshaw_man")
async def rickshaw_man(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLRICKSHAWMAN.c#L241
    Integer is always positive (1 to 100) but this does not mean it is bullish: rickshaw man shows uncertainty
    """
    return await get_result("CDLRICKSHAWMAN", True, False,request)

@app.post("/rising_falling_three_methods")
async def rising_falling_three_methods(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLRISEFALL3METHODS.c#L237
    Integer is positive (1 to 100) or negative (-1 to -100)
    """
    return await get_result("CDLRISEFALL3METHODS", True, True,request)

@app.post("/separating_lines")
async def separating_lines(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLSEPARATINGLINES.c#L236
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
    """
    return await get_result("CDLSEPARATINGLINES", True, True,request)


@app.post("/shooting_star")
async def shooting_star(request: Request):
    """
    Link to the core: 
    https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLSHOOTINGSTAR.c#L237
    Integer is negative (-1 to -100): shooting star is always bearish;
    """
    return await get_result("CDLSHOOTINGSTAR", True, True,request)