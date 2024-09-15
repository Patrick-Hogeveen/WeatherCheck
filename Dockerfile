FROM python:3.11-alpine

# Set up environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the port your application will run on
EXPOSE 5000
RUN python -m flask --app weather init-db
# Specify the command to run on container start
CMD ["python", "-m", "flask", "--app", "weather", "run", "--host=0.0.0.0"]
