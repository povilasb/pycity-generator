from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class CodeCity(Base):
    """City table model."""
    __tablename__ = 'tb_city'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tooltip = Column(String)


    def __repr__(self):
        """
        Returns:
            str: object representation.
        """
        return '<CodeCity(id=%d, name="%s", tooltip="%s")>' % (\
            self.id, self.name, self.tooltip)


class District(Base):
    """City district table model."""
    __tablename__ = 'tb_district'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    tooltip = Column(String)
    city_id = Column(Integer, ForeignKey('tb_city.id'), nullable=False)
    district_id = Column(Integer, ForeignKey('tb_district.id'))


class Building(Base):
    """Building table model."""
    __tablename__ = 'tb_building'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Integer)
    width = Column(Integer)
    color = Column(String)
    tooltip = Column(String)
    district_id = Column(Integer, ForeignKey('tb_district.id'))


class City:
    def __init__(self, host, username, password, database):
        engine = create_engine('mysql://%s:%s@%s/%s' \
            % (username, password, host, database))
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def create_city(self, name):
        """Create new row in city table.

        Args:
            name (str): code city name.

        Returns:
            int: created city id.
        """
        return self._insert(CodeCity(name=name, tooltip=name))


    def create_district(self, name, city_id, parent_district_id=None,
            color='0xD9534F'):
        return self._insert(District(name=name, tooltip=name, color=color,
            city_id=city_id, district_id=parent_district_id))


    def create_building(self, name, height, width, district_id,
            color='0x337AB7'):
        return self._insert(Building(name=name, tooltip=name, color=color,
            district_id=district_id, height=height, width=width))


    def _insert(self, row):
        """Inserts row into DB.

        Returns:
            int inserted row id.
        """
        self.session.add(row)
        self.session.commit()
        return row.id
