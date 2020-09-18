FROM bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8

RUN apt-get update && \
    apt-get -y install \
    build-essential checkinstall \
    libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev \
    wget tar

RUN cd /opt
RUN wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
RUN tar xzf Python-3.8.5.tgz
RUN cd Python-3.8.5 && ./configure --enable-optimizations && make install
RUN cd /opt 
RUN rm -f Python-3.8.5.tgz

RUN ln -s /usr/local/bin/python3 /usr/bin/python3
RUN ln -s /usr/bin/python3 /usr/bin/python