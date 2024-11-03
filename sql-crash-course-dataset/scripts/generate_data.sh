#!/bin/bash

set -euxo pipefail

source .venv/bin/activate

python -m sql_crash_course_dataset --n-users 20000 --n-products 500 --n-orders 5000
