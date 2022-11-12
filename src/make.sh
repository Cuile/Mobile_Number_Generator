#! /bin/sh

pyinstaller --onefile \
            --noconfirm \
            --paths . \
            --distpash ../data/bin \
            --workpath ../data/build \
            --hidden-import encodings.idna \
            --name mng \
            --clean \
            main.py