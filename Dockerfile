# Base image with Python 3.9.16
FROM python:3.9.16

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Jupyter Notebook port
EXPOSE 8888

# Launch Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
