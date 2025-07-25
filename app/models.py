from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime, UTC


class Country(SQLModel, table=True):
    country_id: Optional[int] = Field(default=None, primary_key=True)
    country_uuid: UUID = Field(default_factory=uuid4, nullable=False, unique=True)
    country_name: str = Field(nullable=False)
    country_code: str = Field(min_length=2, max_length=2, nullable=False)  # ISO 3166-1 alpha-2
    currency: Optional[str] = Field(default=None)
    flag: Optional[str] = Field(default=None)

    regions: List["StateOrRegion"] = Relationship(back_populates="country")
    cities: List["City"] = Relationship(back_populates="country")
    provinces: List["Province"] = Relationship(back_populates="country")


class StateOrRegion(SQLModel, table=True):
    state_or_region_id: Optional[int] = Field(default=None, primary_key=True)
    state_or_region_uuid: UUID = Field(default_factory=uuid4, nullable=False, unique=True)
    country_id: int = Field(foreign_key="country.country_id", nullable=False)
    state_or_region_name: str = Field(nullable=False)

    country: Optional[Country] = Relationship(back_populates="regions")
    provinces: List["Province"] = Relationship(back_populates="region")
    cities: List["City"] = Relationship(back_populates="region")


class Province(SQLModel, table=True):
    province_id: Optional[int] = Field(default=None, primary_key=True)
    country_id: int = Field(foreign_key="country.country_id", nullable=False)
    province_uuid: UUID = Field(default_factory=uuid4, nullable=False, unique=True)
    state_or_region_id: int = Field(foreign_key="stateorregion.state_or_region_id")
    province_name: str = Field(nullable=False)

    region: Optional[StateOrRegion] = Relationship(back_populates="provinces")
    cities: List["City"] = Relationship(back_populates="province")
    country: Optional[Country] = Relationship(back_populates="provinces")



class City(SQLModel, table=True):
    city_id: Optional[int] = Field(default=None, primary_key=True)
    city_uuid: UUID = Field(default_factory=uuid4, nullable=False, unique=True)
    country_id: int = Field(foreign_key="country.country_id", nullable=False)
    state_or_region_id: int = Field(foreign_key="stateorregion.state_or_region_id")
    province_id: Optional[int] = Field(default=None, foreign_key="province.province_id")
    city_name: str = Field(nullable=False)
    postal_code: Optional[str] = Field(default=None)

    region: Optional[StateOrRegion] = Relationship(back_populates="cities")
    province: Optional[Province] = Relationship(back_populates="cities")
    localities: List["Locality"] = Relationship(back_populates="city")
    country: Optional[Country] = Relationship(back_populates="cities")


class Locality(SQLModel, table=True):
    locality_id: Optional[int] = Field(default=None, primary_key=True)
    locality_uuid: UUID = Field(default_factory=uuid4, nullable=False, unique=True)
    city_id: int = Field(foreign_key="city.city_id")
    locality_name: str = Field(nullable=False)
    postal_code: Optional[str] = Field(default=None)
    local_label: Optional[str] = Field(default=None)

    city: Optional[City] = Relationship(back_populates="localities")
