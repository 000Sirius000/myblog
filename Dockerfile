FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Застосувати міграції й зібрати статику
RUN python manage.py migrate --no-input
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "myblog.wsgi:application", "--bind", "0.0.0.0:8000"]