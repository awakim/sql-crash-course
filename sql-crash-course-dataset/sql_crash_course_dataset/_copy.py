import pathlib

import duckdb
import pyarrow as pa


def arrow_table_to_parquet(arrow_table: pa.Table, filename: str) -> int:

    pth = pathlib.Path('./dataset')
    pth.mkdir(exist_ok=True)
    for file in pth.glob(f'{filename}.parquet'):
        file.unlink()

    QUERY = """
    COPY
        arrow_table -- duckdb understands this is a python variable
    TO E'./dataset/{filename}'
    (FORMAT PARQUET, OVERWRITE_OR_IGNORE true)
    """
    # DuckDB is capable of accessing Arrow tables/Dataframes directly
    # from python global variables. This is is a very powerful feature.
    num_rows = duckdb.execute(QUERY.format(filename=filename)).fetchone()
    return 0 if num_rows is None else num_rows[0]
