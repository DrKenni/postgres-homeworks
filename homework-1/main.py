"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import psycopg2
import csv

PASS = os.getenv('MY_PASS')

with psycopg2.connect(host="localhost",
                      database="north",
                      user="postgres",
                      password=PASS
                      ) as conn:

    with open('north_data/customers_data.csv', 'r', encoding='windows-1251') as f:
        reader = csv.DictReader(f)
        for row in reader:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                            (row['customer_id'], row['company_name'], row['contact_name']))

    with open('north_data/employees_data.csv', 'r', encoding='windows-1251') as f:
        reader = csv.DictReader(f)
        for row in reader:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO employees(employee_id, first_name, last_name, title, birth_date, notes) "
                            "VALUES (%s, %s, %s, %s, %s, %s)",
                            (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date']))

    with open('north_data/orders_data.csv', 'r', encoding='windows-1251') as f:
        reader = csv.DictReader(f)
        for row in reader:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO orders(order_id, customer_id, employee_id, order_date, ship_city) "
                            "VALUES (%s, %s, %s, %s, %s)",
                            (row['order_id'], row['customer_id'], row['employee_id'],
                             row['order_date'], row['ship_city']))
