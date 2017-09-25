#!/usr/bin/env bash
pid=0

# SIGUSR1-handler
my_handler() {
  echo "my_handler"
}

# SIGTERM-handler
term_handler() {
    if [ ${pid} -ne 0 ]; then
        kill -SIGTERM "${pid}"
        wait "${pid}"
    fi
    # exit 143; # 128 + 15 -- SIGTERM
    exit 0;
}

int_handler() {
    if [ ${pid} -ne 0 ]; then
        kill -SIGINT "${pid}"
        wait "${pid}"
    fi
    # exit 143; # 128 + 15 -- SIGTERM
    exit 0;
}


stop_handler() {
    if [ ${pid} -ne 0 ]; then
        kill -SIGSTOP "${pid}"
        wait "${pid}"
    fi
}

cont_handler() {
    if [ ${pid} -ne 0 ]; then
        kill -SIGCONT "${pid}"
        wait "${pid}"
    fi
}

# setup envionment variables
export DOCKER_BRIDGE_IP=`/sbin/ip route|awk '/default/ { print $3 }'`

# setup handlers
# on callback, kill the last background process, which is `tail -f /dev/null` and execute the specified handler
trap 'kill ${!}; my_handler' SIGUSR1
trap 'kill ${!}; term_handler' SIGTERM
trap 'kill ${!}; int_handler' SIGINT
trap 'kill ${!}; stop_handler' SIGSTOP
trap 'kill ${!}; cont_handler' SIGCONT