# Boston College Machine Intelligence Group (BCMIG) Official Website

This repository hosts the official website for the **Boston College Machine Intelligence Group (BCMIG)**. It is a Django-based web application designed to provide information about the group, events, and research.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [License](#license)

## Project Overview
The **BCMIG Website** is the online presence of the Machine Intelligence Group at Boston College. It serves as a platform to:
- Showcase upcoming events.
- Publish research and blog posts.
- Provide information about the group members and their achievements.
- Connect students and faculty with machine learning and AI opportunities.

## Features
- **Dynamic Content Management**: Add and manage events, blog posts, and member profiles via the Django admin interface.
- **Responsive Design**: Works seamlessly across desktops and mobile devices.
- **Searchable Blog**: Posts are categorized and searchable for easy access to content.
- **Contact Form**: Users can reach out directly from the site.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django 5.0.7 (Python)
- **Database**: SQLite (for local development), PostgreSQL (for production)
- **Hosting**: Render.com


## Environment Variables

The following environment variables should be set in your `.env` file or in Render's dashboard for secure deployment:

- `DJANGO_SECRET_KEY`: A unique secret key for Django.
- `DEBUG`: Set to `False` in production.
- `DATABASE_URL`: The URL of the production database (PostgreSQL for Render).

## Deployment

We are using **Render** for deployment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
