import numpy as np
def lab(x,y):
    """ lab function is used to convert life ration continuous values to categorical values.
    
        Parameters
        ----------
        x = Engine life ratio column
        y = Engine dataframe
     """
    labels = []
    for i in range(0,len(y)):
        if np.array(y[x])[i] <= 0.6:
            labels.append(0)
        elif np.array(y[x])[i] <= 0.8:
            labels.append(1)
        else:
            labels.append(2)
    return labels


def life_ratio(x,y):
    """ Life_ratio function is used to caluclate life ration of engine with the help of Cycle and RUL Columns.
    
        Parameters
        ----------
        x = Engine Cycle
        y = Remaining useful life of engine
        
    """
    life_r = []
    life_r = x/y
    return life_r


def RUl(x,y,df):
    """ Calculating remaining useful life with the help of ID and cycle columns
        where it takes a count of the cycles of perticular engine ID.
        
        Parameters
        ----------
        x = Engine ID Columns
        y = Engine Cycle
        df = Engine DataFrame
    """
    RUL_L = []
    for i in df[x]:
        RUL_L.append(((df[df[x] == i][y]).values)[-1])
    return RUL_L