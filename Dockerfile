FROM python:3.10

WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all files (including your .pkl or .joblib model)
COPY . .

# Setting FLASK_APP to your filename (usually app.py)
ENV FLASK_APP=app.py

# Run with Gunicorn on the Hugging Face port 7860
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]