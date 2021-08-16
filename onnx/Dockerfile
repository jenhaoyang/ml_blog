FROM nvidia/cuda:11.4.1-cudnn8-devel-ubuntu20.04

WORKDIR /app
RUN apt update
RUN apt install -y python3.8
RUN apt install -y build-essential python3.8-dev python3-pip 
RUN pip3 install onnxruntime-gpu
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install  -r /tmp/requirements.txt

USER root
#CMD ["sh","-c","ray start --head && uvicorn WebApp:app"]
#CMD ["sh","-c","uvicorn WebApp:app"]
CMD "/bin/bash"