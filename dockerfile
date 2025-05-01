# 👣 1. Base image with Python
FROM python:3.11-slim

# 🏠 2. Set working directory inside the container
WORKDIR /app

# 📦 3. Copy the bot folder into the container
COPY . /app

# 🧹 4. Install dependencies (optional: check if you have a requirements.txt!)
RUN pip install --upgrade pip \
   && pip install --no-cache-dir -r requirements.txt

# If you have dependencies, add:
# COPY Bots/code-coffee-feed-fetcher/requirements.txt .
# RUN pip install -r requirements.txt

# 🏁 5. Run the bot
CMD ["python", "main.py"]
