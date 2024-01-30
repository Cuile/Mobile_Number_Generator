#!/bin/bash

PROXY="https://github.jobcher.com/gh/" && \
docker compose -f ../docker/start.yml \
                run --rm \
                --entrypoint "python main.py" \
                mobile_number_generator \
                "$@"