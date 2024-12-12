Overview
========

Welcome to Astronomer! This project contains the code shown in the Quickstart ETL with Airflow video series. 

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. 
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.

How to use this repo
====================

1. Fork this repo to your GitHub account.

2. Clone the forked repo to your local machine.

3. Make sure you have the [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli/) installed on your machine.

4. Navigate to the root of the cloned repository and start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

5. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

6. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

7. Define a connection to a Postgres database in the Airflow UI. To do so, navigate to Admin > Connections and click '+'. Fill in the following fields:

- Conn Id: my_postgres_conn
- Conn Type: Postgres
- Host: your Postgres host 
- Database: your Postgres database
- Login: your Postgres username
- Password: your Postgres password
- Port: your Postgres port

8. Run the DAG by unpausing it in the Airflow UI.

Deploy Your Project to Astronomer
=================================

Running this DAG in the cloud is simple, just sign up for a [free Astro trial](https://astronomer.io/try-astro) and follow the instructions to create your first Astro Deployment mapped to a GitHub repository. Add the DAG and SQL files from this repo to the one mapped to your deployment, and Astro will automatically sync the files to your Deployment. Lastly, recreate the Postgres connection in the [Astro Environment Manager](https://www.astronomer.io/docs/astro/manage-connections-variables/#astro-environment-manager) and run the DAG.

Contact
=======

The Astronomer CLI is maintained with 💜 by the Astronomer team. To report a bug or suggest a change, reach out to our support.
