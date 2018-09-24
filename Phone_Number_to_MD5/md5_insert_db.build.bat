docker container run ^
        -it ^
        --rm ^
        -v "%cd%":/root ^
        -w /root ^
        python-dev-env:1 ^
        pyinstaller --onefile --name md5_insert_db --paths . --noconfirm --clean md5_insert_db.py