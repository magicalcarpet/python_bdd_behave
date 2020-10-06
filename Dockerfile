FROM python:3.8-alpine

WORKDIR /python_bdd/

COPY . /python_bdd/

RUN apk update \
    && apk upgrade \
    && apk add bash \
    && pip3 --version \
    && echo "Ruby Tuesday" \
    && pip3 install pipenv \
    && echo "Call The Piper" \
    && pipenv install -r requirements.txt

# This is a work in progress. 
# All dependencies are installed but the container keeps exiting.

# always use double quotes in the CMD bracket
CMD ["/bin/bash"]
