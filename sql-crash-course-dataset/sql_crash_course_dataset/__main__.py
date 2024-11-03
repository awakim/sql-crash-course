import logging
from sql_crash_course_dataset import _defs, _cli, _copy


LOGGER = logging.getLogger(__name__)


def main():
    config = _cli.parse_config()
    LOGGER.info(
        "Will generate dataset with %d users, %d products, and %d orders",
        config.n_users,
        config.n_products,
        config.n_orders
    )

    data_generator = _defs.DataGenerator()
    users = data_generator.generate_users(n=config.n_users)
    products = data_generator.generate_products(n=config.n_products)
    orders = data_generator.generate_orders(
        n=config.n_orders,
        n_users=config.n_users,
        n_products=config.n_products,
    )

    filename = "users.parquet"
    n_users = _copy.arrow_table_to_parquet(users, filename)
    LOGGER.info("Copied %d users to %s", n_users, filename)
    if n_users != config.n_users:
        LOGGER.error("Failed to generate %d users", config.n_users)
        raise RuntimeError(f"Failed to generate {config.n_users} users")

    filename = "products.parquet"
    n_products = _copy.arrow_table_to_parquet(products, filename)
    LOGGER.info("Copied %d products to %s", n_products, filename)
    if n_products != config.n_products:
        LOGGER.error("Failed to generate %d products", config.n_products)
        raise RuntimeError(f"Failed to generate {config.n_products} products")

    filename = "orders.parquet"
    n_orders = _copy.arrow_table_to_parquet(orders, filename)
    LOGGER.info("Copied %d orders to %s", n_orders, filename)
    if n_orders != config.n_orders:
        LOGGER.error("Failed to generate %d orders", config.n_orders)
        raise RuntimeError(f"Failed to generate {config.n_orders} orders")

    LOGGER.info("Done!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    main()
