
# System Requirements Document - School Shuttle Management System

## Functional Requirements

| **#** | **Requirement** | **Acceptance Criteria** |
|-------|-----------------|-------------------------|
| 1     | The system shall allow parents and students to view real-time shuttle locations on a map. | Map updates every 5 seconds with the current location pin visible. |
| 2     | The system shall send automated notifications when the shuttle is approaching the pickup or drop-off point. | Notifications are triggered within a 500-meter radius of the location. |
| 3     | The system shall allow administrators to add, edit, or delete shuttle routes. | Route changes are reflected across all apps within 1 minute. |
| 4     | The system shall provide AI-powered route optimization for shuttles. | Optimized route is generated within 10 seconds upon admin request. |
| 5     | The system shall allow shuttle drivers to log in and view their daily assigned routes. | Driver dashboard shows route details and student list. |
| 6     | The system shall allow drivers to update shuttle status (e.g., "En Route", "Arrived", "Delayed"). | Status changes are reflected in real-time on all user dashboards. |
| 7     | The system shall allow school administrators to view shuttle performance reports. | Reports include trip duration, fuel usage, and delays. |
| 8     | The system shall allow parents to receive emergency alerts in case of delays or breakdowns. | Alerts are sent to affected users within 1 minute of the incident being reported. |
| 9     | The system shall enable administrators to assign drivers to specific shuttle routes. | Assignment is logged and reflected in driver profiles. |
| 10    | The system shall allow new students to register and select default pickup/drop-off locations. | Location info is saved and editable by both admin and parent. |

---

## Non-Functional Requirements

### Usability
- The interface shall support both English and one local language.
- The mobile app shall comply with WCAG 2.1 accessibility standards to accommodate users with disabilities.

### Deployability
- The system shall be deployable on AWS cloud infrastructure using Docker containers.
- The mobile application shall support both Android and iOS platforms.

### Maintainability
- All APIs shall be documented using Swagger/OpenAPI.
- System logs shall be automatically stored and accessible for technical troubleshooting.

### Scalability
- The system shall support up to 10,000 concurrent users.
- The backend infrastructure shall auto-scale during peak usage times (e.g., school start/end).

### Security
- All user data shall be encrypted using AES-256 encryption standards.
- The system shall use JWT-based authentication and role-based access control.

### Performance
- Real-time GPS location updates shall be delivered within 5 seconds of the actual location change.
- Route optimization algorithms shall return results within 10 seconds.
