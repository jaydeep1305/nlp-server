# Python Project Setup

This guide will help you set up a Python virtual environment and install all the required dependencies for the project.

## Prerequisites

Make sure you have Python installed on your system. You can check if Python is installed by running the following command in your terminal or command prompt:

```bash
python --version


## Step 1: Create a Virtual Environment

py -m venv env


## Step 2: Activate the Virtual Environment

.\env\Scripts\activate

## On macOS/Linux:
source env/bin/activate


## Step 3: Install Dependencies
pip install -r requirements.txt

## Step 4: Verify Installation
pip list


## Step 4: Create a .env File for Google Cloud Credentials

GOOGLE_APPLICATION_CREDENTIALS='./path/to/your/keyfile.json'

## Step 5: Initialize Google Cloud SDK

gcloud init

## Step 6: Start Flask Development Server
python app.py


## Step 7: open swagger doc

http://127.0.0.1:5000/documentation

```
