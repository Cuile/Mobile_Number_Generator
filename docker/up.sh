# /bin/bash
cp ../src/requirements.txt .
docker compose -f start.yml up -d
rm requirments.txt
# docker system prune
