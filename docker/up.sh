# /bin/bash

# cp ../src/requirements.txt .
docker compose -f start.yml run --rm mobile_number_generator
# rm requirements.txt
# docker system prune
