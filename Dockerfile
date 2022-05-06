FROM python:3.10-slim
COPY ./main.py .
RUN apt update && apt install -y python3-opencv && pip install opencv-python
ENTRYPOINT ["python", "main.py"]

