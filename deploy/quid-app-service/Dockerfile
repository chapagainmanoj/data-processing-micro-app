FROM quay.io/grepsr/altos-service-py-base:latest

ENV BUILD_DEPS="git-core curl openssh-client unzip g++ curl"

ENV SERVICE_NAME="quid-app-service"
ENV APP_NAME="quid"

RUN apt-get -y update \
    && apt-get -y install -o Dpkg::Options::="--force-confold" --no-install-recommends nodejs $BUILD_DEPS \
    && curl -sL https://deb.nodesource.com/setup_7.x | bash - \
    && apt-get -y install nodejs \
    && pip install --no-cache-dir -U gunicorn==19.7.1 gevent==1.2.1

COPY deploy/webapp-service/scripts/*.sh /usr/local/bin/
COPY requirements.pip /tmp/requirements.txt

RUN pip install --no-cache-dir -U -r /tmp/requirements.txt \
    && apt-get purge -y --auto-remove $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R grepsr:grepsr /home/grepsr \
    && chmod 755 /usr/local/bin/*.sh

USER grepsr
WORKDIR /home/grepsr/$SERVICE_NAME

ENTRYPOINT ["run_webapp.sh"]