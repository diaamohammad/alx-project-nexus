# 🚀 Nexus E-Commerce API

## 📌 Project Overview
Nexus is a robust, scalable backend system designed for modern e-commerce platforms. It manages **Users**, **Products**, and **Categories** with high security and performance.
This project serves as the Capstone Project for the **ProDev Backend Engineering Program**.

## 🛠 Tech Stack
* **Framework:** Django & Django REST Framework (DRF)
* **Database:** PostgreSQL (Production) / SQLite (Dev)
* **Containerization:** Docker & Docker Compose
* **Documentation:** Swagger / OpenAPI
* **CI/CD:** GitHub Actions

## ✨ Key Features
1.  **User Authentication:** Secure Registration & JWT Login.
2.  **Role-Based Access:**
    * **Admin:** Full CRUD capabilities.
    * **User:** Read-only access to products.
3.  **Advanced Product Catalog:**
    * Filtering by Price & Category.
    * Search by Name & Description.
    * Ordering capabilities.
4.  **Performance:** Database indexing for fast queries.

## 🚀 How to Run with Docker (Recommended)
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/alx-project-nexus.git](https://github.com/YOUR_USERNAME/alx-project-nexus.git)
    cd alx-project-nexus
    ```
2.  **Start the application:**
    ```bash
    docker-compose up --build
    ```
3.  **Run Migrations (First time only):**
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```
4.  **Access the API:**
    * Open Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

## 🧪 Running Tests
To run the automated unit tests inside Docker:
```bash
docker-compose exec web python manage.py test