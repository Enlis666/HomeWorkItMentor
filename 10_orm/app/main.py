from models import Orders, Client, Products, Provider, Supply
from crud import create_test_data, create_tables, join_client_employee, CrudClient, AggregatePractice
from models import Employees
from db import session_factory


def select_all_data_table():
    with session_factory() as session:
        clients = session.query(Client).all()
        orders = session.query(Orders).all()
        employees = session.query(Employees).all()
        products = session.query(Products).all()
        providers = session.query(Provider).all()
        supplies = session.query(Supply).all()


        print("Table Orders:")
        for i_order in orders:
            print(i_order)


        print("\nTable Client:")
        for i_client in clients:
            print(i_client)

        print("\nTable Employees:")
        for i_employee in employees:
            print(i_employee)

        print("\nTable Products:")
        for i_product in products:
            print(i_product)

        print("\nTable Provider:")
        for i_provider in providers:
            print(i_provider)

        print("\nTable Supply:")
        for i_supply in supplies:
            print(i_supply)
        print()



if __name__ == "__main__":

    create_tables() # Создание таблиц
    create_test_data() # Создание тестовых данных
    select_all_data_table() # Вовод информации на экран
    join_client_employee() # Объединение двух таблиц и вывод информации на экран
    CrudClient.select_client(1) # Выводим информацию о клиенте
    CrudClient.update_client_phone(1, 9231344500) # Обновляем номер телефона клиента
    print()
    CrudClient.cnt_orders_client() # Считаем кол-во ордеров у клиента
    print()
    AggregatePractice.avg_price() # Средняя цена товаров



