# 🚀 AI-Powered Chat Summarizer

Transform lengthy conversations into clear, concise insights with this AI-driven chat summarization tool! This project fine-tunes Google Pegasus (CNN/Daily Mail) on the Samsum dataset, optimizing it for chat-based text summarization while delivering a seamless user experience through a modern UI.

Followed modular approach from data ingestion-> data transformation-> model trainer-> model evaluation

# 🔥 Key Features

✅ AI-Driven Summarization: Automatically condenses long conversations into meaningful summaries.

✅ Fine-Tuned Model: Uses Google Pegasus (CNN/Daily Mail), optimized with Samsum dataset for chat-based summarization.

✅ High-Performance Results: Ensures accurate, readable, and context-aware summaries.

✅ Beautiful UI: Developed using Flask, HTML, CSS, and JavaScript for an intuitive experience.

# 🛠 Tech Stack

Machine Learning: TensorFlow, Hugging Face Transformers

Model: Google Pegasus fine-tuned on Samsum dataset

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

# Project Worklflow

graph TD;

    A[Chat Input] --> B[Text Processing];
    
    B --> C[Google Pegasus Model];
    
    C --> D[Summarized Output];
    
    D --> E[User Interface];
# Parameters used in training the model

  num_train_epochs: 3
  
  warmup_steps: 500
  
  per_device_train_batch_size: 1
  
  weight_decay: 0.01
  
  logging_steps: 10
  
  evaluation_strategy: steps
  
  eval_steps: 500
  
  save_steps: 500
  
  gradient_accumulation_steps: 16

# Ouptput

->Before Fine Tuning

![image](https://github.com/user-attachments/assets/59bd6099-fdc4-433c-94fc-645ff2b91096)


->After fine tuning

![image](https://github.com/user-attachments/assets/eb9132c2-d825-4e36-9c38-5124f0c5d16b)

    
