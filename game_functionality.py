import math
import matplotlib
import tiles
from random import choice
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# engine = create_engine('sqlite:////tmp/teste.db', echo=True)
# Base = declarative_base(bind=engine)

def main():
    
    random_tile = tiles.Tile()
    
    cold_tile = tiles.Tile("Michael Dresser", "wl")
    
    print(random_tile)
    print(cold_tile)
    
    input()
    
if __name__ == "__main__":
    main()