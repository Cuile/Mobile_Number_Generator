#!/bin/bash

PROXY="https://github.jobcher.com/gh/"
docker compose run --rm \
                -f ../docker/start.yml \
                --entrypoint "python main.py" \
                mobile_number_generator \
                "$@"