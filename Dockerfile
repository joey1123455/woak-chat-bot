# Set the base image
FROM rasa/rasa:latest-full

# Set the working directory
WORKDIR /app

# Copy the entire project directory into the Docker image
COPY . .

# Switch to root user
USER root

# Train the Rasa models with root permissions
RUN rasa train

# Switch back to the default non-root user
USER 1001

# Expose the Rasa server port
EXPOSE 5005

# Start the Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
