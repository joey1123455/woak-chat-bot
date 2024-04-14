# Stage 1: Build Rasa models
FROM rasa/rasa:latest-full as builder

# Set the working directory
WORKDIR /app

# Copy only the necessary files for training
COPY data ./data
COPY config.yml ./

# Train the Rasa models
RUN rasa train

# Stage 2: Runtime
FROM rasa/rasa:latest

# Set the working directory
WORKDIR /app

# Copy trained models from the builder stage
COPY --from=builder /app/models ./models

# Expose the Rasa server port
EXPOSE 5005

# Start the Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
