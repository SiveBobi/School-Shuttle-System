# 📦 Product Backlog

This product backlog supports the School Shuttle Management System and is structured using MoSCoW prioritization, effort estimation, and known task dependencies.

---

| **Story ID** | **User Story**                                                                 | **Priority (MoSCoW)** | **Effort Estimate** | **Dependencies**                    |
|--------------|----------------------------------------------------------------------------------|------------------------|---------------------|-------------------------------------|
| US01         | As a parent, I want to receive a notification when the shuttle is nearby        | Must Have              | 8 Story Points       | US04 (Shuttle Status Updates)       |
| US02         | As a student, I want to view the shuttle’s real-time location                   | Must Have              | 13 Story Points      | Google Maps API                     |
| US03         | As an admin, I want to assign a driver to a shuttle route                       | Must Have              | 5 Story Points       | None                                |
| US04         | As a driver, I want to update the shuttle’s status (e.g., “En Route”, “Delayed”)| Must Have              | 3 Story Points       | None                                |
| US05         | As a parent, I want to register my child for the shuttle                        | Should Have            | 5 Story Points       | None                                |
| US06         | As an admin, I want to use AI to optimize shuttle routes                        | Could Have             | 13 Story Points      | Student data + Location data        |
| US07         | As a driver, I want to view my daily assigned routes                            | Must Have              | 5 Story Points       | US03 (Driver Assignment)            |
| US08         | As an admin, I want to view shuttle performance reports                         | Could Have             | 8 Story Points       | Logging module                      |
