from datetime import datetime

from aiohttp.log import client_logger
from sqlalchemy import func, select, update, delete
from sqlalchemy.orm import aliased
from yappi import start

from db import session_factory
from db import Base, engine
from models import Orders, Employees, Products, Supply, Provider, Client


class CrudProvider:
    @staticmethod
    def delete_providers(provider_ids):
        with session_factory() as session:
            delete_query = delete(Provider).where(Provider.id_provider.in_(provider_ids))
            session.execute(delete_query)
            session.commit()

            select_query = select(Provider)
            result = session.execute(select_query)

            remaining_providers = result.scalars().all()
            
            for provider in remaining_providers:
                print(provider)


class AggregatePractice:
    @staticmethod
    def avg_price():
        with session_factory() as session:
            query = (
                select(Products.name_of_product, func.avg(Products.selling_price))
                .group_by(Products.name_of_product)
            )
            result  = session.execute(query)
            for name_of_product, avg_price in result:
                print(f'Product: {name_of_product}, Average Price: {avg_price}')

class CrudClient:
    @staticmethod
    def select_client(id_c):
        with session_factory() as session:
            query = select(Client).where(Client.id==id_c)
            result = session.execute(query)
            print(f'\nClient №{id_c}: \n {result.scalars().first()}')


    @staticmethod
    def update_client_phone(id_c,val):
        with session_factory() as session:
            query = select(Client).where(Client.id==id_c)
            result = session.execute(query)
            client = result.scalars().first()
            print(f'\nДанные до обновления: {client}')
            client.phone = val
            print(f'Данные после обновления: {client}')
            session.commit()

    @staticmethod
    def cnt_orders_client():
        with session_factory() as session:
            query =(
                select(Client.full_name, func.count(Orders.id_order).label("order_count"))
                .join(Orders, Client.id == Orders.id_client)
                .where(Orders.execution_date >= "2024-01-01")
                .group_by(Client.id)
                .order_by(func.count(Orders.id_order).desc())
            ).distinct()

            result = session.execute(query)
            clients_with_order_counts = result.all()
            for client, order_count in clients_with_order_counts:
                print(f'Client: {client}, Orders Count: {order_count}')


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def join_client_employee():
    with session_factory() as session:
        query = session.query(
            Client.full_name.label("client_name"),
            func.concat(Employees.surname, ' ', Employees.name).label("employee_name")
        ).join(Orders, Orders.id_client == Client.id) \
            .join(Employees, Orders.id_employee == Employees.id_employee)

        result = query.all()

        with session_factory() as session:
            query = session.query(
                Client.full_name.label("client_name"),
                func.concat(Employees.surname, ' ', Employees.name).label("employee_name")
            ).join(Orders, Orders.id_client == Client.id) \
                .join(Employees, Orders.id_employee == Employees.id_employee)

            result = query.all()

            for row in result:
                print(f'client: {row[0]} | employee: {row[1]}')


def create_test_data():
    with session_factory() as session:
        # Тестовые данные для таблицы Employees
        employees = [
            Employees(id_employee=1, family="Ivanov", name="Ivan", surname="Ivanovich", job_title="Manager",
                      address="Moscow", home_phone="123456789", birthday=datetime(1990, 1, 1)),
            Employees(id_employee=2, family="Petrov", name="Petr", surname="Petrovich", job_title="Developer",
                      address="Saint Petersburg", home_phone="987654321", birthday=datetime(1992, 2, 2)),
            Employees(id_employee=3, family="Sidorov", name="Sidr", surname="Sidorovich", job_title="Designer",
                      address="Novosibirsk", home_phone="555555555", birthday=datetime(1993, 3, 3)),
            Employees(id_employee=4, family="Smirnov", name="Alex", surname="Alexandrovich", job_title="Analyst",
                      address="Yekaterinburg", home_phone="444444444", birthday=datetime(1988, 4, 4)),
            Employees(id_employee=5, family="Kuznetsov", name="Nikita", surname="Nikitich", job_title="Tester",
                      address="Kazan", home_phone="666666666", birthday=datetime(1985, 5, 5)),
        ]
        session.add_all(employees)

        # Тестовые данные для таблицы Products
        products = [
            Products(id_product=1, id_supply=1, name_of_product="Laptop", specifications="16GB RAM, 512GB SSD",
                     description="High-performance laptop", image=None, purchase_cost=700.0,
                     availability=20, quantity=15, selling_price=850.0),
            Products(id_product=2, id_supply=1, name_of_product="Smartphone", specifications="128GB Storage",
                     description="Latest smartphone model", image=None, purchase_cost=300.0,
                     availability=50, quantity=30, selling_price=400.0),
            Products(id_product=3, id_supply=2, name_of_product="Tablet", specifications="10-inch display",
                     description="Portable tablet for everyday use", image=None, purchase_cost=200.0,
                     availability=25, quantity=10, selling_price=250.0),
            Products(id_product=4, id_supply=2, name_of_product="Headphones", specifications="Noise cancelling",
                     description="Wireless over-ear headphones", image=None, purchase_cost=150.0,
                     availability=15, quantity=20, selling_price=200.0),
            Products(id_product=5, id_supply=3, name_of_product="Smartwatch", specifications="Fitness tracking",
                     description="Smartwatch with fitness tracking features", image=None, purchase_cost=100.0,
                     availability=40, quantity=25, selling_price=130.0),
        ]
        session.add_all(products)

        # Тестовые данные для таблицы Clients
        clients = [
            Client(id=1, full_name="Alexey Ivanov", address="Moscow", phone="123456789"),
            Client(id=2, full_name="Maria Petrova", address="Saint Petersburg", phone="987654321"),
            Client(id=3, full_name="Sergey Sidorov", address="Novosibirsk", phone="555555555"),
            Client(id=4, full_name="Elena Smirnova", address="Yekaterinburg", phone="444444444"),
            Client(id=5, full_name="Dmitry Kuznetsov", address="Kazan", phone="666666666"),
        ]
        session.add_all(clients)

        # Тестовые данные для таблицы Providers
        providers = [
            Provider(id_provider=1, name_of_provider="Provider One", representative="John Doe",
                     speak_to="Jane Doe", phone="111222333", address="Provider Address 1"),
            Provider(id_provider=2, name_of_provider="Provider Two", representative="Alice Smith",
                     speak_to="Bob Brown", phone="222333444", address="Provider Address 2"),
            Provider(id_provider=3, name_of_provider="Provider Three", representative="Charlie Johnson",
                     speak_to="Diana Williams", phone="333444555", address="Provider Address 3"),
            Provider(id_provider=4, name_of_provider="Provider Four", representative="Eva Green",
                     speak_to="Frank White", phone="444555666", address="Provider Address 4"),
            Provider(id_provider=5, name_of_provider="Provider Five", representative="George Black",
                     speak_to="Hannah Grey", phone="555666777", address="Provider Address 5"),
        ]
        session.add_all(providers)

        # Тестовые данные для таблицы Supply
        supplies = [
            Supply(id_supply=1, id_provider=1, data_of_supply=datetime.now()),
            Supply(id_supply=2, id_provider=2, data_of_supply=datetime.now()),
            Supply(id_supply=3, id_provider=3, data_of_supply=datetime.now()),
            Supply(id_supply=4, id_provider=4, data_of_supply=datetime.now()),
            Supply(id_supply=5, id_provider=5, data_of_supply=datetime.now()),
        ]
        session.add_all(supplies)

        # Тестовые данные для таблицы Orders
        orders = [
            Orders(id_order=1, id_employee=1, id_product=1, id_client=1,
                   posting_date=datetime.now(), execution_date=datetime.now()),
            Orders(id_order=2, id_employee=2, id_product=2, id_client=2,
                   posting_date=datetime.now(), execution_date=datetime.now()),
            Orders(id_order=3, id_employee=3, id_product=3, id_client=3,
                   posting_date=datetime.now(), execution_date=datetime.now()),
            Orders(id_order=4, id_employee=4, id_product=4, id_client=4,
                   posting_date=datetime.now(), execution_date=datetime.now()),
            Orders(id_order=5, id_employee=5, id_product=5, id_client=5,
                   posting_date=datetime.now(), execution_date=datetime.now()),
        ]

        session.add_all(orders)
        session.commit()


