# /bin/bash

docker compose -f start.yml \
    run --rm \
        --entrypoint "python main.py" \
        mobile_number_generator \
        "$@"