#!/usr/bin/env bash
source /usr/local/bin/run_handler.sh
gunicorn app:app -w 2 --bind 0.0.0.0:8080 --log-level=debug -t 120 --reload &
pid="$!"
wait ${!}