FROM python:3.11-alpine

RUN apt-get add dos2unix

RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir --upgrade setuptools
	&& pip install --no-cache-dir pyinstaller==3.4

# RUN echo "export PS1='[\A \u@\H \w]\\$ '" >> $HOME/.bashrc \
# 	&& echo "alias ll='ls -lh --color'" >> $HOME/.bashrc

CMD ["/bin/sh"]