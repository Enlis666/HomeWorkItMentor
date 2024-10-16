from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime, date

from db import Base


class Orders(Base):
    __tablename__ = "Orders"
    __table_args__ = {"extend_existing": True, }

    id_order: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_employee: Mapped[int] = mapped_column(ForeignKey("Employees.id_employee"))
    id_product: Mapped[int] = mapped_column(ForeignKey("Products.id_product"))
    id_client: Mapped[int] = mapped_column(ForeignKey("Client.id"))
    posting_date: Mapped[Optional[datetime]]
    execution_date: Mapped[Optional[datetime]]

    employee: Mapped["Employees"] = relationship(back_populates="orders")
    products: Mapped["Products"] = relationship(back_populates="orders")
    client: Mapped["Client"] = relationship(back_populates="orders")



    def __repr__(self):
        return (f"Orders(id_order = {self.id_order}, id_employee = {self.id_employee},"
                f"id_product = {self.id_product}, id_client = {self.id_client},"
                f"posting_date = {self.posting_date}, execution_date = {self.execution_date})")


class Employees(Base):

    __tablename__ = 'Employees'
    __table_args__ = {"extend_existing": True, }

    id_employee: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    family: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]
    job_title: Mapped[str]
    address: Mapped[str]
    home_phone: Mapped[str]
    birthday: Mapped[date]

    orders: Mapped[List["Orders"]] = relationship(back_populates="employee")

    def __repr__(self):
        return (f"Employees(id_employee = {self.id_employee}, family = {self.family}"
                f"name = {self.name}, surname = {self.surname}"
                f"job_title = {self.job_title}, address = {self.address})"
                f"home_phone = {self.home_phone}, birthday = {self.birthday})")


class Products(Base):
    __tablename__ = 'Products'
    __table_args__ = {"extend_existing": True, }

    id_product: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_supply: Mapped[int] = mapped_column(ForeignKey('Supply.id_supply'))
    name_of_product: Mapped[str]
    specifications: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    image: Mapped[Optional[str]]
    purchase_cost: Mapped[float]
    availability: Mapped[int]
    quantity: Mapped[int]
    selling_price: Mapped[float]

    supply: Mapped['Supply'] = relationship(back_populates="products")
    orders: Mapped[List['Orders']] = relationship(back_populates="products")

    def __repr__(self):
        return (f"Products(id_product={self.id_product}, name_of_product={self.name_of_product}, "
                f"purchase_cost={self.purchase_cost}, selling_price={self.selling_price})")


class Supply(Base):
    __tablename__ = 'Supply'
    __table_args__ = {"extend_existing": True, }

    id_supply: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_provider: Mapped[int] = mapped_column(ForeignKey('Provider.id_provider'))
    data_of_supply: Mapped[datetime]

    provider: Mapped['Provider'] = relationship(back_populates="supply")
    products: Mapped[List['Products']] = relationship(back_populates="supply")

    def __repr__(self):
        return f"Supply(id_supply={self.id_supply}, data_of_supply={self.data_of_supply})"


class Provider(Base):
    __tablename__ = 'Provider'
    __table_args__ = {"extend_existing": True, }

    id_provider: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_of_provider: Mapped[str]
    representative: Mapped[Optional[str]]
    speak_to: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]
    address: Mapped[Optional[str]]

    supply: Mapped[List['Supply']] = relationship(back_populates="provider")

    def __repr__(self):
        return f"Provider(id_provider={self.id_provider}, name_of_provider={self.name_of_provider})"


class Client(Base):
    __tablename__ = 'Client'
    __table_args__ = {"extend_existing": True, }

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str]
    address: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]

    orders: Mapped[List['Orders']] = relationship(back_populates="client")

    def __repr__(self):
        return f"Client(id={self.id}, full_name={self.full_name}, phone={self.phone})"
