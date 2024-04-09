# Use an official node runtime as a parent image
FROM node:14

# Set the working directory
WORKDIR /app/

# Copy package.json and yarn.lock files to the container
COPY package.json yarn.lock /app/

# Install dependencies
RUN npm install

# Copy the rest of the frontend code to the container
COPY . /app/

# Build static files
RUN yarn build

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
