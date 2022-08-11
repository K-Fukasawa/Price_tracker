# This is the test to make sure the dataframes are not empty and if filled, are float.

from price_tracker_L7 import df7
from price_tracker_L8 import df8
from price_tracker_L9 import df9


def test_list():
    assert df7.empty == False
    assert isinstance(df7.iat[0,0], float) == True
    assert isinstance(df7.iat[0,1], float) == True
    assert isinstance(df7.iat[0,2], float) == True
    assert isinstance(df7.iat[0,3], float) == True
    assert isinstance(df7.iat[1,0], float) == True
    assert isinstance(df7.iat[1,1], float) == True
    assert isinstance(df7.iat[1,2], float) == True
    assert isinstance(df7.iat[1,3], float) == True
    assert isinstance(df7.iat[2,0], float) == True
    assert isinstance(df7.iat[2,1], float) == True
    assert isinstance(df7.iat[2,2], float) == True
    assert isinstance(df7.iat[2,3], float) == True

    assert df8.empty == False
    assert isinstance(df8.iat[0,0], float) == True
    assert isinstance(df8.iat[0,1], float) == True
    assert isinstance(df8.iat[0,2], float) == True
    assert isinstance(df8.iat[0,3], float) == True
    assert isinstance(df8.iat[1,0], float) == True
    assert isinstance(df8.iat[1,1], float) == True
    assert isinstance(df8.iat[1,2], float) == True
    assert isinstance(df8.iat[1,3], float) == True
    assert isinstance(df8.iat[2,0], float) == True
    assert isinstance(df8.iat[2,1], float) == True
    assert isinstance(df8.iat[2,2], float) == True
    assert isinstance(df8.iat[2,3], float) == True

    assert df9.empty == False
    assert isinstance(df9.iat[0,0], float) == True
    assert isinstance(df9.iat[0,1], float) == True
    assert isinstance(df9.iat[0,2], float) == True
    assert isinstance(df9.iat[0,3], float) == True
    assert isinstance(df9.iat[1,0], float) == True
    assert isinstance(df9.iat[1,1], float) == True
    assert isinstance(df9.iat[1,2], float) == True
    assert isinstance(df9.iat[1,3], float) == True
    assert isinstance(df9.iat[2,0], float) == True
    assert isinstance(df9.iat[2,1], float) == True
    assert isinstance(df9.iat[2,2], float) == True
    assert isinstance(df9.iat[2,3], float) == True


