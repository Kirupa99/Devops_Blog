# 1️⃣ Use lightweight Python image
FROM python:3.11-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependencies file
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy all project files
COPY . .

# 6️⃣ Expose port your app will run on
EXPOSE 5000

# 7️⃣ Run the app
CMD ["python", "app.py"]
