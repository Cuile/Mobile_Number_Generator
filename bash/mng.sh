#!/bin/bash

docker compose -f ../docker/start.yml run \
                --build --rm \
                --entrypoint "python main.py" \
                mobile_number_generator \
                "$@"