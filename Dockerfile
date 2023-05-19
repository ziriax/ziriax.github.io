# Use an official Ruby runtime as a parent image
FROM ruby:3.2

# Install Node.js, LaTeX, pandoc
RUN apt-get update -qq && apt-get install -y nodejs texlive-full pandoc

# Install Jekyll and Bundler
RUN gem install jekyll bundler jekyll-latex

# Set the working directory in the container to /app
WORKDIR /app

# Add the src directory contents into the container at /app
ADD . /app

# Set the JEKYLL_ENV environment variable to production
ENV JEKYLL_ENV=production

# Install any needed packages specified in Gemfile
RUN bundle install

# Update the bundle
RUN bundle update

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV NAME World

# Run jekyll when the container launches
CMD ["bundle", "exec", "jekyll", "serve", "--force_polling", "--livereload", "--host", "0.0.0.0"]


