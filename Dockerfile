# Use Python 3.12 official image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY . /app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

# # Set environment variables for Flask
# ENV FLASK_APP=app.py \
#     FLASK_RUN_HOST=0.0.0.0 \
#     FLASK_RUN_PORT=5000

# # Expose port 5000 for Flask
# EXPOSE 5000

# # Run the application
# CMD ["python", "app.py"]


# FROM python:3.12

# # The two following lines are requirements for the Dev Mode to be functional
# # Learn more about the Dev Mode at https://huggingface.co/dev-mode-explorers
# RUN useradd -m -u 1000 user
# WORKDIR /app

# COPY --chown=user ./requirements.txt requirements.txt
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# COPY --chown=user . /app

# USER user

# ENV HOME=/home/user \
# 	PATH=/home/user/.local/bin:$PATH

# EXPOSE 5000
# CMD ["python", "app.py"]
