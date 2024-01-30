#!/bin/bash

docker compose -f ../docker/start.yml \
            run --rm --entrypoint "python main.py" \
            mobile_number_generator \
            "$@"