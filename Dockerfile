# Set the base image
FROM rasa/rasa:latest-full

# Set the working directory
WORKDIR /app

# Copy the entire project directory into the Docker image
COPY . .

# Adjust permissions of config.yml
RUN chmod +w config.yml

# Train the Rasa models
RUN rasa train

# Expose the Rasa server port
EXPOSE 5005

# Start the Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
