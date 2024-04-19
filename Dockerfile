FROM python:3.11

COPY . .

RUN pip install -r requirements.txt

CMD ["nohup", "shiny", "run", "shinysearch/app.py"]

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]