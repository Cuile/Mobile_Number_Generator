# /bin/bash
cp ../src/requirements.txt .
docker compose -f start.yml up -d
# docker system prune
