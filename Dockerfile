FROM python:3

ARG APP_FOLDER

WORKDIR /usr/src/$APP_FOLDER

COPY ./ ./

RUN pip install --no-cache-dir -r source/requirements.txt

CMD [ "python", "./source/main.py" ]

#EXPOSE 8080