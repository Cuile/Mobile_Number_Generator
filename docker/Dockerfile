FROM python:3.11.3-alpine

# RUN apt-get install -y binutils libc6 libc-bin

# RUN pip install --no-cache-dir pyinstaller==3.4
COPY ./requirements.txt /tmp/requirements.txt 
RUN pip install --no-cache-dir -r /tmp/requirements.txt 

# RUN echo "export PS1='[\A \u@\H \w]\\$ '" >> $HOME/.bashrc \
# 	&& echo "alias ll='ls -lh --color'" >> $HOME/.bashrc

CMD ["/bin/sh"]