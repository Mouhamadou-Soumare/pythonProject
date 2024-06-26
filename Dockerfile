# Use the official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies

RUN apt-get update \
    && apt-get install -y gcc mariadb-client libmariadb-dev \
                          libssl-dev libffi-dev python3-dev \
                          default-libmysqlclient-dev \
                          pkg-config \
    && apt-get clean

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
# Set working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade typing-extensions

# Copy the rest of the application code
COPY . .

# Copy the populate_data script
COPY populate_data.py .

# Expose port 80 (FastAPI default)
EXPOSE 80

# Command to run the application
CMD ["/wait-for-it.sh", "mariadb:3306", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
