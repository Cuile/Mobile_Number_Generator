:: debug:
docker container run ^
        -it ^
        --rm ^
        -v "%cd%"\src:/root/code ^
        -v D:\Data_Label\:/root/data ^
        -w /root/code ^
        md5.collision:1
