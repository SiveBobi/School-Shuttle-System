# 📘 API Documentation (Swagger / OpenAPI)

## Swagger UI Link

FastAPI automatically generates API documentation using the OpenAPI standard.

Once the app is running, open:

📌 Swagger UI:  
http://localhost:8000/docs

📌 ReDoc UI:  
http://localhost:8000/redoc

---

## Example:

- View all routes grouped by entity (Books, Users, Loans)
- Test requests directly from the browser
- Auto-validates schemas and shows errors (e.g. 404, 400)

---

## Optional: OpenAPI Spec Export

To export the raw OpenAPI spec:

```bash
http GET http://localhost:8000/openapi.json > openapi.json
