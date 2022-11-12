#! /bin/sh

pyinstaller --onefile \
            --noconfirm \
            --paths . \
            --distpash ./bin \
            --workpath ./build \
            --hidden-import encodings.idna \
            --name mng \
            --clean \
            main.py