# Base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies (includes PyYAML)
RUN pip install -U pip && pip install -r requirements.txt PyYAML

# Run sanity suite with HTML report
CMD ["python", "-m", "src.orchestrator.cli", "--suite", "sanity", "-n", "2", "--html", "sanity.html"]
