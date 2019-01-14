#! /bin/sh

pyinstaller --onefile \
            --noconfirm \
            --clean \
            --paths . \
            --distpash ../bin \
            --workpath ../build \
            --hidden-import encodings.idna \
            --name 2hash \
            --clean \
            2md5.py