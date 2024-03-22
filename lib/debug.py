from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Playlist, Song

if __name__ == '__main__':

    db_path = '../lib/soundsphere.db'

    engine = create_engine(f'sqlite:///{db_path}')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb
    ipdb.set_trace()
