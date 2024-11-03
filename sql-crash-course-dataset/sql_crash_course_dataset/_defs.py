import datetime

import pyarrow as pa
from faker import Faker
import random

Faker.seed(0)
random.seed(42)

USERS_START_DATE = datetime.datetime(2020, 1, 1)
USERS_END_DATE = datetime.datetime(2023, 1, 1)

# Solves inconsistency in the dates for the orders
# The orders should be generated after the users
# for the orders not to have dates before the users
ORDERS_START_DATE = datetime.datetime(2024, 1, 1)
ORDERS_END_DATE = datetime.datetime(2024, 12, 31)


class DataGenerator:
    def __init__(self) -> None:
        self.faker = Faker()

    def generate_users(self, n: int) -> pa.Table:
        return pa.Table.from_pydict(
            {
                'user_id': pa.array(i + 1 for i in range(n)),
                'username': pa.array(self.faker.user_name() for _ in range(n)),
                'email': pa.array(self.faker.email() for _ in range(n)),
                'first_name': pa.array(self.faker.first_name() for _ in range(n)),
                'last_name': pa.array(self.faker.last_name() for _ in range(n)),
                'address': pa.array(self.faker.address().replace('\n', ', ') for _ in range(n)),
                'created_at': pa.array(self.faker.date_time_between_dates(datetime_start=USERS_START_DATE, datetime_end=USERS_END_DATE) for _ in range(n)),
            }
        )

    def generate_products(self, n: int) -> pa.Table:
        return pa.Table.from_pydict(
            {
                'product_id': pa.array(i + 1 for i in range(n)),
                'product_name': pa.array(f"{self.faker.word().capitalize()} {self.faker.word().capitalize()}" for _ in range(n)),
                'price': pa.array(round(random.uniform(5.0, 100.0), 2) for _ in range(n)),
                'category': pa.array(random.choice(['Tech', 'Clothing', 'Food', 'Books']) for _ in range(n)),
                'stock': pa.array(random.randint(0, 500) for _ in range(n)),
            }
        )

    def generate_orders(self, n: int, n_users: int, n_products: int) -> pa.Table:
        return pa.Table.from_pydict(
            {
                'order_id': pa.array(i + 1 for i in range(n)),
                'user_id': pa.array(random.randint(1, n_users) for _ in range(n)),
                'product_id': pa.array(random.randint(1, n_products) for _ in range(n)),
                'quantity': pa.array(random.randint(1, 5) for _ in range(n)),
                'order_date': pa.array(self.faker.date_time_between_dates(datetime_start=ORDERS_START_DATE, datetime_end=ORDERS_END_DATE) for _ in range(n)),
                'status': pa.array(random.choice(['PENDING', 'SHIPPED', 'DELIVERED', 'CANCELLED']) for _ in range(n)),
            }
        )
