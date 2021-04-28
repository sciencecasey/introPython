import pandas as pd
path = "../miniconda3/envs/introPython/practice&tutorial_src/nba_all_elo.csv"
nba = pd.read_csv(path)
type(nba)
nba.shape
nba.head()
nba.tail(3)
nba.info()
nba.sum()
nba.describe()

        
    
