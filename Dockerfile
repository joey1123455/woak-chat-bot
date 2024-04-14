# Set the base image
FROM rasa/rasa:latest-full

# Set the working directory
WORKDIR /app

# Copy all necessary files
COPY data ./data
COPY config.yml ./

# Train the Rasa models
RUN rasa train

# Create the models directory
RUN mkdir -p /app/models

# Copy trained models
COPY ./models ./models

# Expose the Rasa server port
EXPOSE 5005

# Start the Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
