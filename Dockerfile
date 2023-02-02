FROM python:3.9-alpine3.13

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# # Set the environment variables for Django
# ENV DJANGO_SETTINGS_MODULE=your_project.settings
# ENV DJANGO_SECRET_KEY=secret_key

# Run migrations and start the server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
