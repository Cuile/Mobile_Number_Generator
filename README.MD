## 一、直接使用

命令行参数直接传递给镜像里的程序，直接生成结果。
```bash
$ cd docker

$ sh mng.sh -h
$ sh mng.sh make_ragne -h
$ sh mng.sh make_ragne -r 135 -p ../data
```
相关技术请参阅：
- [Dockerfile: ENTRYPOINT和CMD的区别](https://zhuanlan.zhihu.com/p/30555962)
- [docker compose run](https://docs.docker.com/engine/reference/commandline/compose_run/)
- [Shell 传递参数](https://www.runoob.com/linux/linux-shell-passing-arguments.html)

## 二、编译使用

运行编译好的文件时，如果碰到下面的报错，说明需要升级 glibc 包的版本。
```bash
Error loading Python lib '/tmp/_MEIa23XFM/libpython3.7m.so.1.0': dlopen: /lib64/libc.so.6: version `GLIBC_2.28' not found (required by /tmp/_MEIa23XFM/libpython3.7m.so.1.0)
```

### 升级到glibc-2.28

```bash
$ cd ~
$ wget https://mirror.bjtu.edu.cn/gnu/libc/glibc-2.28.tar.xz
$ mkdir glibc-2.28
$ tar -xf glibc-2.28.tar.xz -C /usr/local
$ cd glibc-2.28
$ mkdir build
$ cd build/
$ ../configure --prefix=/root/glibc-2.28
# 运行时间较长，可能会有半小时
$ make
$ make install

$ cd ~
$ rm -rf glibc-2.28*

# 出现下面报错信息，是 make bison compiler 版本太老，需要升级
configure: error: 
*** These critical programs are missing or too old: make bison compiler
*** Check the INSTALL file for required versions.

# 升级 make
$ cd ~
$ wget http://ftp.gnu.org/gnu/make/make-4.2.tar.gz
$ tar -xzvf make-4.2.tar.gz
$ cd make-4.2
$ ./configure
$ make
$ make install
$ rm -rf /usr/bin/make
$ cp ./make /usr/bin/
$ make -v
GNU Make 4.2
为 x86_64-pc-linux-gnu 编译
Copyright (C) 1988-2016 Free Software Foundation, Inc.
许可证：GPLv3+：GNU 通用公共许可证第 3 版或更新版本<http://gnu.org/licenses/gpl.html>。
本软件是自由软件：您可以自由修改和重新发布它。
在法律允许的范围内没有其他保证。

$ cd ~
$ rm -rf make-4.2*

# 安装 bison
$ yum install -y bison

# 升级 gcc 编译器
$ yum -y install centos-release-scl
$ yum -y install devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-binutils
$ scl enable devtoolset-8 bash
$ echo "source /opt/rh/devtoolset-8/enable" >>/etc/profile
```