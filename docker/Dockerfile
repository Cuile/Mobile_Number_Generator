FROM python:3.7-alpine

RUN apk add dos2unix binutils libc6 libc-bin

RUN pip install --no-cache-dir pyinstaller==3.4

# RUN echo "export PS1='[\A \u@\H \w]\\$ '" >> $HOME/.bashrc \
# 	&& echo "alias ll='ls -lh --color'" >> $HOME/.bashrc

CMD ["/bin/sh"]