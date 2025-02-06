from sqlalchemy import Column, Integer, BigInteger, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.repository.db_connection import DbConnection

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(BigInteger, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    position = Column(Enum("1", "2", "3", "4", "5", name="position_enum"), nullable=False)
    mmr = Column(Integer, default=500)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    abandons = Column(Integer, default=0)
    
    def __repr__(self):
        return (f"<Player(id={self.id}, discord_id={self.discord_id}, name='{self.name}', "
                f"position='{self.position}', mmr={self.mmr}, wins={self.wins}, "
                f"losses={self.losses}, abandons={self.abandons})>")

class PlayerPersistence(DbConnection):
    def __init__(self):
        super().__init__()
        self.engine = self.get_db_engine()
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def add_player(self, discord_id, name, position, mmr=500, wins=0, losses=0, abandons=0):
        session = self.Session()
        try:
            player = Player(
                discord_id=discord_id,
                name=name,
                position=position,
                mmr=mmr,
                wins=wins,
                losses=losses,
                abandons=abandons
            )
            session.add(player)
            session.commit()
            return player
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def find_by_discord_id(self, discord_id):
        session = self.Session()
        try:
            player = session.query(Player).filter_by(discord_id=discord_id).first()
            return player
        finally:
            session.close()

    def get_all_players(self):
        """Retorna todos os jogadores do banco de dados"""
        session = self.Session()
        try:
            return session.query(Player).all()
        finally:
            session.close()

    def update_player(self, discord_id, **kwargs):
        session = self.Session()
        try:
            player = session.query(Player).filter_by(discord_id=discord_id).first()
            if player:
                for key, value in kwargs.items():
                    if hasattr(player, key):
                        setattr(player, key, value)
                session.commit()
                return player
            return None
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_player(self, discord_id):
        session = self.Session()
        try:
            player = session.query(Player).filter_by(discord_id=discord_id).first()
            if player:
                session.delete(player)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
