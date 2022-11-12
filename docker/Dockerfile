FROM python:3.7-buster

RUN apt-get install -y dos2unix binutils

RUN pip install --no-cache-dir pyinstaller==3.4

# RUN echo "export PS1='[\A \u@\H \w]\\$ '" >> $HOME/.bashrc \
# 	&& echo "alias ll='ls -lh --color'" >> $HOME/.bashrc

CMD ["/bin/sh"]