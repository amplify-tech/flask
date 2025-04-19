# Use a slim, secure base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port for Cloud Run or local use
EXPOSE 5000

# Run with Gunicorn
CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:5000"]
