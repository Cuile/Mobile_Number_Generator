#!/bin/bash

docker compose -f ../docker/start.yml \
        rm -f python_base \
&& \
docker compose -f ../docker/start.yml \
        run --rm --entrypoint "python -m cProfile -s cumtime src/main.py" \
            mobile_number_generator "$@"