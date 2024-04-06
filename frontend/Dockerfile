# Use an official node runtime as a parent image
FROM node:14

# Set the working directory
WORKDIR /app/frontend

# Copy package.json and yarn.lock files to the container
COPY package.json yarn.lock /app/frontend/

# Install dependencies
RUN yarn install

# Copy the rest of the frontend code to the container
COPY . /app/frontend

# Build static files
RUN yarn build

# Have to move all static files other than index.html to root/
# for whitenoise middleware
WORKDIR /app/frontend/build

# Move static files to the root directory
RUN mkdir /app/root \
    && mv /app/frontend/build/* /app/root/

# Change working directory to root
WORKDIR /app/root

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["yarn", "start"]
