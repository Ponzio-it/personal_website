# My Personal Portfolio Website

This is the source code for my personal portfolio website, built with Django, JavaScript, and React. This website showcases my projects, skills, and background, offering an interactive platform for visitors to learn more about my work and connect with me.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Roadmap](#project-roadmap)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

---

## Features

- **Dynamic Project Showcase**: Displays portfolio projects organized by category with detailed descriptions, technologies used, and links to live demos or GitHub repositories.
- **File Management System**: Organizes project resources using a folder and file structure, supporting both public and private file access.
- **Responsive Design**: Built to provide an optimal experience across various devices, from mobile phones to desktops.
- **Contact Page**: Allows visitors to send messages directly through the site.

---

## Project Structure

The project is organized into the following main components:

- **portfolio**: Django app that handles views, models, and templates for the portfolio content.
  - **models.py**: Defines the `Project`, `Folder`, and `File` models, allowing flexible organization of portfolio items.
  - **views.py**: Contains view logic for serving pages like `home`, `about_me`, `projects`, and `contact`.
  - **templates/portfolio**: HTML templates for rendering each page.
  - **static/portfolio**: Static assets including CSS, JavaScript, and images.

---

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, React
- **Database**: SQLite (default for Django)
- **Others**: Bootstrap for styling, Git for version control

---

## Setup and Installation

To get a local copy up and running, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ponzio-it/personal_website.git
   cd personal_website
