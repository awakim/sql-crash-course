# SQL Crash Course Dataset
In this repository you'll find the minimum scripts to generate the data for the Introduction to SQL crash course.

It requires you to have [python](https://mise.jdx.dev/lang/python.html), [poetry](https://python-poetry.org/docs/) and [DuckDB](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager) installed in your system.

## Dataset Generation

The dataset is purely synthetic and generated using the [Faker](https://faker.readthedocs.io/en/master/) library.

If you want to reproduce, you can:
- Install dependencies
```bash
poetry install
```

- Generate the data:
```bash
bash ./scripts/generate_data.sh
```

That's it! You should have the data in the [dataset](./dataset/) folder.

# Dataset Exploration

You can explore the dataset by running the following command:

```bash
ls dataset/
orders.parquet   products.parquet users.parquet
```

```bash
duckdb -c "DESCRIBE SELECT * FROM 'dataset/users.parquet';"
┌─────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│ column_name │ column_type │  null   │   key   │ default │  extra  │
│   varchar   │   varchar   │ varchar │ varchar │ varchar │ varchar │
├─────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ user_id     │ BIGINT      │ YES     │         │         │         │
│ username    │ VARCHAR     │ YES     │         │         │         │
│ email       │ VARCHAR     │ YES     │         │         │         │
│ first_name  │ VARCHAR     │ YES     │         │         │         │
│ last_name   │ VARCHAR     │ YES     │         │         │         │
│ address     │ VARCHAR     │ YES     │         │         │         │
│ created_at  │ TIMESTAMP   │ YES     │         │         │         │
└─────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┘
```

Now, see you in the [course](../README.md)! 🚀