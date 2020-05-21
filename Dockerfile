FROM python:3.7
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY app.py /app
COPY model.hdf5 /app
CMD ["python", "app.py"]
