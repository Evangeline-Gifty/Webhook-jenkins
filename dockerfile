FROM Python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["Python", "app.py"]

