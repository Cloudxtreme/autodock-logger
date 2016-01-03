FROM prologic/python-runtime:2.7

ENTRYPOINT ["autodock-logger"]
CMD []

RUN apk -U add git

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /app
COPY . /app/
RUN pip install .
