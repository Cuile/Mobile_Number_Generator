#! /bin/sh

pyinstaller --onefile \
            --noconfirm \
            --clean \
            --paths . \
            --distpash . \
            --workpath ../build \
            --hidden-import encodings.idna \
            --name mng \
            --clean \
            main.py