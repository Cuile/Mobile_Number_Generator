#!/bin/bash

docker compose -f ../docker/start.yml \
                run --rm \
                mobile_number_generator