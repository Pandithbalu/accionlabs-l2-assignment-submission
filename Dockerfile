# secure base image
FROM nginx:1.19-alpine

# Label
LABEL maintainer="bip@exa.com"
LABEL description="Nginx 1.19 Container"

# Remove default nginx config if needed (optional)
# RUN rm /etc/nginx/conf.d/default.conf

# Copy custom config if you have one (optional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# sytart the process in foreground

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
