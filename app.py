import json
from talib import abstract
import talib
from fastapi import FastAPI, Request
import pandas as pd
from ta import add_all_ta_features

app = FastAPI()


@app.get("/")
def test_ground():
    data = pd.read_csv("./data.csv")
    df  = pd.DataFrame(data)
    df['time'] =  pd.to_datetime(df['time'], unit='s')

    candlesticks = [method for method in dir(abstract) if method.startswith('CDL')]
    for candlestick in candlesticks:
        df[str(candlestick)] = getattr(abstract, candlestick)(df)
    print(df.head(20))
    print('---' * 20)
    # df.rename(columns={'real_volume': 'volume'}, inplace=True)
    # print(df.head(20))
    # print('---' * 20)
    # df = apply_all_ta_methods(df)
    # print(df.head(20))
    # print('---' * 20)
    # Convert the result to a DataFrame and assign column names
    df[['Aroon_Up', 'Aroon_Down']] = getattr(abstract, "AROON")(df)
    df['APO'] = getattr(abstract, "APO")(df, fastperiod=12, slowperiod=26, matype=0)
    df['Three_Inside_Up_Down'] = getattr(abstract, 'CDLADVANCEBLOCK')(df)
    df = add_all_ta_features(df, open="open", high="high", low="low", close="close", volume="real_volume", fillna=True)
    # df['Two_Crows'] = getattr(abstract, "CDL2CROWS")(df)
    print(df.tail(50))
    print('---' * 20)
    print(df.describe())
    # print(talib.get_function_groups().keys())
    # patterns = talib.get_function_groups()['Pattern Recognition']
    # print('*** ' * 20)
    # print(patterns)
    # usable = []
    # for pattern in patterns:
    #     pattern = str(pattern)
    #     if df[pattern].mean() != 0:
    #         usable.append(pattern)
    # print(f"-----------------------------------------------{len(usable)}/{len(patterns)}: {len(df)}-------------------------------------------------------------------------------------------------------------------------")
    # print(usable)
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
    




@app.post("/three_inside_up_down")
async def three_inside_up_down(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3INSIDE.c#L222
    Integer is positive (1 to 100) for the three inside up or negative (-1 to -100) for the three inside down; 
    """
    # get the OHLC from MT5
    candles = await request.body()
    # turn the bytes to string
    candles=candles.decode('utf8').replace("'", '"')
    # turn the string to json
    candles = json.loads(candles)
    # create a df
    df = pd.DataFrame(candles)
    # Three inside up or down 
    df['Three_Inside_Up_Down'] = getattr(abstract, 'CDL3INSIDE')(df)
    # get the 
    last_element = df['Three_Inside_Up_Down'].iloc[-1]
    if 0 < last_element <= 100:
        return "up"
    elif  0 > last_element >= -100:
        return "down"
    else:
        return "none"
    

@app.post("/three_line_strike")
async def three_inside_up_down(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3LINESTRIKE.c#L224C10-L224C68
    Integer is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;

    """
    # get the OHLC from MT5
    candles = await request.body()
    # turn the bytes to string
    candles=candles.decode('utf8').replace("'", '"')
    # turn the string to json
    candles = json.loads(candles)
    # create a df
    df = pd.DataFrame(candles)
    # Three inside up or down 
    df['Three_Line_Strike'] = getattr(abstract, 'CDL3LINESTRIKE')(df)
    # get the 
    last_element = df['Three_Line_Strike'].iloc[-1]
    if 0 < last_element <= 100:
        return "up"
    elif  0 > last_element >= -100:
        return "down"
    else:
        return "none"
        
    

@app.post("/three_outside_up_or_down")
async def three_outside_up_or_down(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3OUTSIDE.c#L211C10-L211C117
    Integer is positive (1 to 100) for the three outside up or negative (-1 to -100) for the three outside down
    """
    # get the OHLC from MT5
    candles = await request.body()
    # turn the bytes to string
    candles=candles.decode('utf8').replace("'", '"')
    # turn the string to json
    candles = json.loads(candles)
    # create a df
    df = pd.DataFrame(candles)
    # Three inside up or down 
    df['Three_Line_Strike'] = getattr(abstract, 'CDL3OUTSIDE')(df)
    # get the 
    last_element = df['Three_Line_Strike'].iloc[-1]
    if 0 < last_element <= 100:
        return "up"
    elif  0 > last_element >= -100:
        return "down"
    else:
        return "none"
        
    
    
@app.post("/three_advancing_white_soldiers")
async def three_advancing_white_soldiers(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3WHITESOLDIERS.c#L260
    Integer is positive (1 to 100): advancing 3 white soldiers is always bullish;
    """
    # get the OHLC from MT5
    candles = await request.body()
    # turn the bytes to string
    candles=candles.decode('utf8').replace("'", '"')
    # turn the string to json
    candles = json.loads(candles)
    # create a df
    df = pd.DataFrame(candles)
    # Three inside up or down 
    df['Three_Line_Strike'] = getattr(abstract, 'CDL3WHITESOLDIERS')(df)
    # get the 
    last_element = df['Three_Line_Strike'].iloc[-1]
    if 0 < last_element <= 100:
        return "up"
    else:
        return "none"
    
    
@app.post("/three_advanced_blocks")
async def three_advanced_blocks(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDLADVANCEBLOCK.c#L260
    Integer is negative (-1 to -100): two crows is always bearish; 
    """
    return await get_result("CDLADVANCEBLOCK", False, True,request)


    
@app.post("/two_crows")
async def two_crows(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL2CROWS.c#L222
    Integer is negative (-1 to -100): advance block is always bearish;
    """
    return await get_result("CDL2CROWS", False, True,request)


@app.post("/three_stars_in_the_south")
async def three_stars_in_the_south(request: Request):
    """
    Link to the core: https://github.com/TA-Lib/ta-lib/blob/main/src/ta_func/ta_CDL3STARSINSOUTH.c#L249
    Integer is positive (1 to 100): 3 stars in the south is always bullish;
    """
    return await get_result("CDL3STARSINSOUTH", True, False,request)