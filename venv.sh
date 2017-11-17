#!/usr/bin/env bash
DIRECTORY=virtualenvs/.quid
deactivate 2> /dev/null
if [ -d "${DIRECTORY}" ]; then
    source ${DIRECTORY}/bin/activate
else
    virtualenv -p `which python3` ${DIRECTORY}
    source ${DIRECTORY}/bin/activate
fi
export SENDGRID_API_KEY='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'
