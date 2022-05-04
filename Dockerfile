FROM ubuntu:18.04
RUN apt update && apt upgrade -y
RUN apt install -y python  python-pip
RUN mkdir -p /home/ubuntu/app
COPY src/requirements.txt /home/ubuntu/app/
RUN pip install -r /home/ubuntu/app/requirements.txt
# VOLUME [ "app" ]
WORKDIR /home/ubuntu/app/
ENTRYPOINT [ "python"]
CMD [ "emailwatch.py" ]