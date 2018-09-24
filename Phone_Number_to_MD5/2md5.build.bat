docker container run ^
        -it ^
        --rm ^
        -v "%cd%":/root ^
        -w /root ^
        python-dev-env:1 ^
        pyinstaller --onefile --name 2md5 --paths . --noconfirm --clean 2md5.py