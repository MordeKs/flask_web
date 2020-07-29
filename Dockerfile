FROM amancevice/pandas:0.23.0-python3-alpine

RUN echo 'http://mirrors.aliyun.com/alpine/v3.8/main' > /etc/apk/repositories
RUN echo '@community http://mirrors.aliyun.com/alpine/v3.8/community' >> /etc/apk/repositories
RUN echo '@testing http://mirrors.aliyun.com/alpine/edge/testing' >> /etc/apk/repositories

RUN apk update && apk upgrade
ENV TIMEZONE Asia/Shanghai
RUN apk add tzdata bash curl gcc musl-dev libxml2 libxslt libxml2-dev libxslt-dev libcurl libffi-dev
RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime
RUN echo $TIMEZONE > /etc/timezone
RUN  if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN mkdir -p /root/.pip
COPY pip.conf /root/.pip/
ENV PYCURL_SSL_LIBRARY=openssl
RUN apk add build-base curl-dev
RUN pip install --upgrade pip
RUN pip install pymongo  && \
    pip install kafka-python && \
    pip install xlrd && \
    pip install beautifulsoup4 && \
    pip install mysql-connector-python && \
    pip install mysql-connector-python-rf==2.0.4 && \
    pip install PyMySQL  && \
    pip install selenium && \
    pip install numpy && \
    pip install amqp && \
    apk add nodejs  && \
    apk add npm && \
    npm install pm2 -g && \
    pip install  pykafka  && \
    pip install pymysql && \
    pip install requests && \
    pip install redis && \
    pip install pyyaml && \
    pip install apscheduler && \
    pip install DBUtils && \
    pip install elasticsearch==6.3.1 && \
    mkdir -p /opt/python
ADD .  /opt/python/python/
RUN pip install request flask flasgger flask_cors -i https://mirrors.aliyun.com/pypi/simple/
COPY start.sh /opt/python/start.sh
RUN chmod -R 777 /opt/python/
CMD ["/opt/python/start.sh"]
