FROM python:slim
LABEL authors="Rajendra Kumar R Yadav"
WORKDIR /app
COPY requirements.txt .
RUN /bin/bash -c "pip install -r requirements.txt"
RUN /bin/bash -c "mkdir -p logs"
COPY messages.proto .
COPY ./proto-compile.py .
RUN /bin/bash -c "python proto-compile.py"
COPY . .
EXPOSE 5000
RUN /bin/bash -c "chmod u+x ./entrypoint.sh"
ENTRYPOINT ["./entrypoint.sh"]