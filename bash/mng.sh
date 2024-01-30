#!/bin/bash

docker compose -f ../docker/start.yml run \
                --rm \
                --env-file=start.env \
                --entrypoint "python main.py" \
                mobile_number_generator \
                "$@"