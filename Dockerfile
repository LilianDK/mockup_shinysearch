FROM python:3.10

# Copy using poetry.lock* in case it doesn't exist yet
COPY . .

RUN pip install -r requirements.txt

# CMD ["tail", "-f", "/dev/null"]
#CMD ["streamlit", "run", "gui.py", "--theme.base=dark"]

ENTRYPOINT ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]