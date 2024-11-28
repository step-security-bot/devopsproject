FROM python:3@sha256:bc78d3c007f86dbb87d711b8b082d9d564b8025487e780d24ccb8581d83ef8b0

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]