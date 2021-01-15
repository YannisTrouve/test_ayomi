# Technical test for AYOMI

## Overview

This app was created for a technical test for AYOMI

## Programming Language

 - Python
 - Javascript

## Features
  This app can :
  - Register a User
  - Log in a User
  - Display User's Fist name/Last name (If filled) and email.
  - Change user's email address
  
## Running this project with docker
  1. Clone this project locally
  2. `cd into the project directory`
  3. Run `sudo docker build -t test_ayomi .` to build the container image.
  4. Run `sudo docker-compose up -d`
  5. Open [0.0.0.0:8000](https://0.0.0.0:8000) to check the app. Check if the port is used. Modify in `docker-compose.yml`
  6. When finish `sudo docker down` will down all the containers or `sudo docker stop <containerid>` and `sudo docker rm <containerid>` for a specific container.
  
