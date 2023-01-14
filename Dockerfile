FROM python:3.8.16-slim-bullseye
WORKDIR /serviceA
COPY ./requirements.txt ./
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt  
COPY ./sender_app.py ./
ENTRYPOINT [ "python3","sender_app.py"]