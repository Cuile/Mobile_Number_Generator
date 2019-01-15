#! /bin/sh

pyinstaller --onefile \
            --noconfirm \
            --clean \
            --paths . \
            --distpash ../bin \
            --workpath ../build \
            --hidden-import encodings.idna \
            --name check_value \
            --clean \
            main.py