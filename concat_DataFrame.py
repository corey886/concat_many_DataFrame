
import pandas as pd
import math

def scFunc02(inputDf):

    try:
        if 0 < len(inputDf) and len(inputDf) <= 2:
            outDf = pd.DataFrame()
            for ii in (range(len(inputDf))):
                if ii == 0:
                    outDf = inputDf.iloc[ii][0]
                else:
                    tmp = inputDf.iloc[ii][0]
                    outDf = pd.concat(
                        [outDf, tmp], ignore_index=True, sort=False)
            return outDf
        elif 2 < len(inputDf):
            cutt = int(math.ceil(len(inputDf)*0.5))
            partA = inputDf.iloc[0:cutt]
            partB = inputDf.iloc[(len(inputDf)-cutt+1):]

            if len(partA) > 0 and len(partB) > 0:
                return pd.concat([scFunc02(partA), scFunc02(partB)], ignore_index=True, sort=False)
            elif len(partA) > 0 and len(partB) == 0:
                return partA
            elif len(partA) == 0 and len(partB) > 0:
                return partB
            elif len(partA) == 0 and len(partB) == 0:
                return pd.DataFrame()

    except:
        print('error scFunc02')

    return pd.DataFrame()