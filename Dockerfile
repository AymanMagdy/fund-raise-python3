FROM python:3
WORKDIR /usr/src/app
COPY fund_project_package .
CMD ["python3", "./main.py"]

