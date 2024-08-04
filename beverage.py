"""Beverage data models"""

# System Imports.
import os

# Third-party imports
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, Float, Boolean

# Base class for other models to inherit from
Base = declarative_base()
engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Beverage(Base):
    """Beverage class"""

    __tablename__ = "beverages"

    id = Column(String(8), primary_key=True)
    name = Column(String(255), nullable=False)
    pack = Column(String(255), nullable=False)
    price = Column(Float(2), nullable=False)
    active = Column(Boolean, nullable=False)

    def __init__(self, id_, name, pack, price, active):
        """Constructor"""
        self.id = id_
        self.name = name
        self.pack = pack
        self.price = price
        self.active = active

    def __str__(self):
        """String method"""
        active = "True" if self.active else "False"
        return f"| {self.id:>6} | {self.name:<56} | {self.pack:<15} | {self.price:>6.2f} | {active:<6} |"


class BeverageRepository:
    """BeverageRepository class"""

    def __str__(self):
        """String method"""
        return_string = ""
        beverages = session.query(Beverage).all()
        for beverage in beverages:
            return_string += f"{beverage}{os.linesep}"
        return return_string

    @property
    def database_exists(self):
        """Return whether the database exists"""
        return os.path.exists("./db.sqlite3")

    def create_database(self):
        """Create the database"""
        Base.metadata.create_all(engine)

    def data_exists(self):
        """Return whether there is already data in the database"""
        return session.query(Beverage).first() is not None

    def item_exists(self, id_):
        """Determine if an item exists in the database"""
        return self.find_by_id(id_) is not None

    def find_by_id(self, id_):
        """Find a beverage by it's id"""
        beverage_to_find = session.query(Beverage).get(id_)
        return beverage_to_find

    def find_by_name(self, search_name):
        """Find a beverage by it's name"""
        beverage_to_find = (
            session.query(
                Beverage,
            )
            .filter(
                Beverage.name == search_name,
            )
            .first()
        )
        return beverage_to_find

    def add(self, id_, name, pack, price, active):
        """Add a new beverage to the database"""
        # Make a new instance of Beverage
        beverage_to_add = Beverage(id_, name, pack, price, active)

        # Add beverage to database and persist the addition
        session.add(beverage_to_add)
        session.commit()

    def update(self, id_, name, pack, price, active):
        """Update an existing beverage with matching id"""
        # Find the beverage to update
        beverage_to_update = self.find_by_id(id_)
        # If the beverage is not None, we can update it
        if beverage_to_update is not None:
            if name is not None:
                beverage_to_update.name = name
            if pack is not None:
                beverage_to_update.pack = pack
            if price is not None:
                beverage_to_update.price = price
            if active is not None:
                beverage_to_update.active = active

            session.commit()
            return True
        else:
            return False

    def delete(self, id_):
        """Delete an existing beverage with matching id"""
        # Find the beverage to delete
        beverage_to_delete = self.find_by_id(id_)
        # If the beverage is not None, we can delete it
        if beverage_to_delete is not None:
            session.delete(beverage_to_delete)
            session.commit()
            return True
        else:
            return False
