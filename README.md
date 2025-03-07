# Generating Process Descriptions with Generative AI - TracEX Fork

[![GitHub stars](https://img.shields.io/github/stars/bptlab/TracEX)](https://github.com/bptlab/TracEX)
[![GitHub open issues](https://img.shields.io/github/issues/bptlab/TracEX)](https://github.com/bptlab/TracEX/issues)
[![GitHub closed pull requests](https://img.shields.io/github/issues-closed/bptlab/TracEX)](https://github.com/bptlab/TracEX/issues)
[![GitHub open pull requests](https://img.shields.io/github/issues-pr/bptlab/TracEX)](https://github.com/bptlab/TracEX/issues)
[![Pylint](https://github.com/bptlab/tracex/actions/workflows/pylint.yml/badge.svg)](https://github.com/bptlab/TracEX/blob/main/.github/workflows/pylint.yml)

This repository is a fork of the original TracEX project and contains the implementation of the bachelor's thesis "Generating Process Descriptions with Generative AI".
It also contains the evaluation data of the thesis and the "Patient Journey" configuration used to produce the presented results.

## Process Description Generation Tool
Follow the setup instructions from the original README below to start the TracEX tool.
Once you are on the landing page you can navigate to the "Process Description Generation" tab.
Here you can select the process description configuration you want to use, the degree of variation between the instances, and the number of instances you want to generate.
You can also specify whether you want to save the generated instances to the database, as text files or at all.
After you have configured the generation process, you can start the generation by clicking the "Generate new Process Description" button.
The generated instances will then be displayed along with the corresponding instance configuration.

If you want to adjust the generation process, you can find all the relevant code in the "tracex_project/patient_journey_generator" directory.
Specifically in generator.py.
There are three main functions responsible for the generation process:
- **execute_generate_process_description():** This function is called when the user starts the generation process. It reads the user input and calls the other two functions accordingly.
- **generate_process_description():** This function generates the process descriptions based on the user input.
- **get_instance_config():** This function determines the instance configuration based on the degree of variation. It implements the configuration matrix of the degree of variation.

## Evaluation Data
The evaluation data used in the thesis can be found in the "evaluation_data" directory.
For each batch of generated process descriptions there is a directory (low, medium, high) with the related process descriptions and their event logs.
All generated journeys, their traces, and event logs are also stored in the database.
You can access these indirectly through the TracEX tool (Database Results -> Evaluation) or directly over the admin page (http://127.0.0.1:8000/admin/, user: admin, password: admin).
In the evaluation view, you can filter for low, medium, and high to see the complete event log and DFG for the respective batch.

## Patient Journey Configuration
The patient journey configuration used in the thesis can be found in "tracex_project/patient_journey_generator/process_description_configurations/patient_journey_configuration.json".
There in the same directory there is an example configuration file for a different domain and case.
When creating a new configuration file, make sure to follow the framework of the thesis and the structure of the existing configuration files.

## Disclaimer
Please note that the TracEX extraction pipeline is currently unable to extract event logs from anything other than patient journeys.
Also, regarding the rest of the README and wiki, the information about the patient journey generator is outdated and does not apply to the process description generation tool.
___

TracEX aims to extract event logs from unstructured text, specifically written patient experiences known as patient journeys. By leveraging Large Language Models (LLMs), TracEX can automatically identify and extract relevant events, activities, timestamps and further information from natural langauge text. This enables healthcare professionals and researchers to gain valuable insights into patient experiences, treatment pathways, and potential areas for improvement in healthcare delivery.

This project was initiated and completed as part of the team's bachelor's degree under the supervision of the Business Process Technology chair at the Hasso Plattner Institute. The project was conducted in cooperation with [mamahealth](https://www.mamahealth.com/).

## Key Features
- **Extraction Pipeline**: A robust pipeline to clean, process, and extract data from natural language text.
- **Patient Journey Generator**: Generates comprehensive patient journeys based on randomized cohort data.
- **Database**: Stores patient journeys and related extraction results for easy access and analysis.
- **Metrics and Evaluation Tool**: Evaluates the accuracy and effectiveness of the extraction process and allows for analysis of exctraction results.
- **Intuitive UI**: User-friendly interface for you to interact with the tool and visualize results.

## Requirements
To run TracEX successfully, it is essential to obtain an OpenAI API key with adequate credits. TracEX integrates the OpenAI API to leverage Large Language Models (LLMs) for extracting relevant information from unstructured text. Without a valid API key and sufficient balance, the extraction process cannot be performed. The current prices for API can be looked up at [OpenAI Pricing](https://openai.com/api/pricing/).

## Installation using Docker
**Option 1: Using a Pre-built Docker Image** \
The easiest way to run a local instance of TracEX is using the provided Docker image.

1. Install Docker: Ensure that you have Docker installed on your system. If you haven't installed it yet, please follow the official Docker installation guide for your operating system.
1. Download the Latest Docker Image: Download the latest TracEX Docker image from the provided link: [docker image](https://github.com/bptlab/TracEX/releases/tag/release)
1. Load the Docker Image: Open a terminal or command prompt and navigate to the directory where you downloaded the Docker image file. Run the following command to load the image: `docker load -i tracex.tar`\
Note: Depending on your system configuration, you may need to run this command with `sudo` privileges.
1. Run the Docker Container: After the image is successfully loaded, run the following command to start the TracEX container: `docker run -p 8000:8000 tracex`\
This command will start the container and map port 8000 from the container to port 8000 on your local machine. Again, you may need to use `sudo` depending on your system setup.
1. Access TracEX: Open a web browser and navigate to http://localhost:8000/. This will bring you to the TracEX application, where you can enter your OpenAI API Key and start extracting event logs.

**Option 2: Building the Docker Image from Source** \
Alternatively, you can build the Docker image from the TracEX source code.

1. Clone the TracEX Repository: Open a terminal or command prompt and navigate to the directory where you want to clone the TracEX repository. Run the following command to clone the repository: `git clone https://github.com/bptlab/TracEX`
1. Navigate to the TracEX Directory: Change your current directory to the cloned TracEX repository: `cd TracEX`
1. Build the Docker Image: Run the following command to build the TracEX Docker image: `docker build -t tracex .`\
Note: Depending on your system configuration, you may need to run this command with `sudo` privileges.
1. Run the Docker Container: After the image is successfully built, run the following command to start the TracEX container: `docker run -p 8000:8000 tracex`\
This command will start the container and map port 8000 from the container to port 8000 on your local machine. Again, you may need to use `sudo` depending on your system setup.
1. Access TracEX: Open a web browser and navigate to http://localhost:8000/. This will bring you to the TracEX application, where you can enter your OpenAI API Key and start extracting event logs.

## Local Setup for Development

### Download

- Use git and run `git clone https://github.com/bptlab/TracEX` in the desired directory _(Using e.g. Git Bash)_

### Installation
- navigate to the root directory of TracEX in your terminal
- run `install-dependencies-unix.sh` or `install-dependencies-windows.ps1`, based on your operating system _(Using e.g. Terminal)_
- If you are using macOS, please use [homebrew](https://brew.sh/) or any other package manager to install the listed dependencies manually
- run `python tracex_project/manage.py migrate` to update the database and apply all changes stored in the `migrations/` folder
- export OpenAI API key as environment variable: `export OPENAI_API_KEY=<API-KEY>`

### Execution
- Run `python tracex_project/manage.py runserver` in the root directory of TracEX _(Using e.g. Terminal)_

### Pre-Commit

- If you intend on expanding the code, please run `pre-commit install` in the root directory of TracEX _(Using e.g. Terminal)_

## Contributors

The main contributors to the project are the six members of the [2023/24 Bachelor Project](https://hpi.de/fileadmin/user_upload/hpi/dokumente/studiendokumente/bachelor/bachelorprojekte/2023_24/BA-Projekt_FG_Weske_Event_Log_Extraction_from_Patient_Experiences.pdf) of Professor Weske's [Business Process Technology Chair](https://bpt.hpi.uni-potsdam.de) at the [Hasso Plattner Institute](https://hpi.de):

- [Pit Buttchereit](https://github.com/PitButtchereit)
- [Frederic Rupprecht](https://github.com/FR-SON)
- [VanThang Nguyen](https://github.com/thangixd)
- [Nils Schmitt](https://github.com/nils-schmitt)
- [Soeren Schubert](https://github.com/soeren227)
- [Trung-Kien Vu](https://github.com/tkv29)

These six participants will push the project forward as part of their bachelor's degree until the summer of 2024.
At the same time our commitment to open source means that we are enabling -in fact encouraging- all interested parties to contribute and become part of its developer community.

## Project documentation

In the project wiki, you can find detailed documentation that covers various aspects of TracEX.
In the [architecture](https://github.com/bptlab/TracEX/wiki/Architecture) section, we provide an overview of the system's design and components. The [repository structure](https://github.com/bptlab/TracEX/wiki/Repository-Structure) is also outlined, making it easier for you to navigate and understand the organization of our codebase.
Most importantly, we have dedicated a significant portion of the wiki to explaining our [pipeline frameworks](https://github.com/bptlab/TracEX/wiki/Pipelines), which are the core of TracEX. These frameworks are responsible for processing and transforming the unstructured patient journey data into structured event logs.
