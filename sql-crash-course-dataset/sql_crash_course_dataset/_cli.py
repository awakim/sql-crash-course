import argparse
from pydantic import BaseModel, PositiveInt


class Config(BaseModel):
    n_users: PositiveInt
    n_products: PositiveInt
    n_orders: PositiveInt


def parse_config() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--n-users',
        type=int,
        default=10000,
        help='Number of users to generate'
    )
    parser.add_argument(
        '--n-products',
        type=int,
        default=1000,
        help='Number of products to generate'
    )
    parser.add_argument(
        '--n-orders',
        type=int,
        default=1000,
        help='Number of orders to generate'
    )

    args = parser.parse_args()

    return Config(
        n_users=args.n_users,
        n_products=args.n_products,
        n_orders=args.n_orders
    )
