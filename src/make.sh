#! /bin/sh

pyinstaller --onefile \
            --noconfirm \
            --paths . \
            --distpath ../bin \
            --workpath ../build \
            --hidden-import encodings.idna \
            --name mng \
            --clean \
            main.py