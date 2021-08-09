FROM alpine:3.10

MAINTAINER Lorenzo Carbonell <a.k.a. atareao> "lorenzo.carbonell.cerezo@gmail.com"

ARG S6_OVERLAY_RELEASE=https://github.com/just-containers/s6-overlay/releases/latest/download/s6-overlay-amd64.tar.gz

ENV S6_OVERLAY_RELEASE=${S6_OVERLAY_RELEASE}
ENV PYTHONUNBUFFERED=1

ADD ${S6_OVERLAY_RELEASE} /tmp/s6overlay.tar.gz
COPY ./src/*.py /app/
COPY ./etc /etc


RUN echo "**** install S6 ****" \
    apk upgrade --update --no-cache \
    && rm -rf /var/cache/apk/* \
    && tar xzf /tmp/s6overlay.tar.gz -C / \
    && rm /tmp/s6overlay.tar.gz
RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN pip3 install --no-cache-dir \
    flask \
    itsdangerous \
    requests \
    pyinotify  \
    werkzeug && \
    rm -rf /var/lib/apt/lists/*
RUN addgroup ebot && \
    adduser -h /app -G ebot -D ebot && \
    chown -R ebot:ebot /app

WORKDIR /app

ENTRYPOINT ["/init"]
