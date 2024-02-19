#!/bin/bash

docker compose -f ../docker/start.yml \
        run --rm --entrypoint "python src/main.py" \
            mobile_number_generator "$@"
docker compose -f ../docker/start.yml \
        rm -f python_base
