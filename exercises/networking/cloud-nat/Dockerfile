FROM python
EXPOSE 8080

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Install Python libraries
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY *.py ./

CMD exec python main.py

