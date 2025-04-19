FROM python:3.11-slim

# Avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Create a non-root user
RUN addgroup --system app && adduser --system --group app

# Install updates & production dependencies only
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y gcc libpq-dev curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Set permissions and switch to non-root
RUN chown -R app:app /app
USER app

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
