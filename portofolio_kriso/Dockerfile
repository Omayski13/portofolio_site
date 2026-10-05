# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean


# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

# Expose port (Fly uses 8080 by default)
EXPOSE 8080


# Copy project files
COPY . .

# Collect static files (optional)
RUN python manage.py collectstatic --noinput

# Run Django via Gunicorn
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn portofolio_kriso.wsgi:application --bind 0.0.0.0:8080"]

