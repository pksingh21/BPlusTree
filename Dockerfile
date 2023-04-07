FROM python:3.8-slim
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
USER app_user
COPY . .
CMD ["bash"]
