
# ✅ Test Cases for School Shuttle Management System

This section provides a set of **functional test cases** that validate the behavior of the system as defined in the use case specifications, as well as **non-functional test scenarios** to validate performance and security aspects.

---

## 🧪 Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|-------------|-------|------------------|----------------|--------|
| TC-001 | FR-001 | View real-time shuttle location | 1. Login <br> 2. Open map view | Location pin appears and updates every 5 seconds | ... | Pass/Fail |
| TC-002 | FR-002 | Receive notifications near pickup point | 1. Save pickup location <br> 2. Shuttle enters 500m radius | Notification is sent to parent device | ... | Pass/Fail |
| TC-003 | FR-003 | Admin adds a new shuttle route | 1. Admin logs in <br> 2. Clicks "Add Route" <br> 3. Inputs details and saves | Route appears in all user dashboards within 1 minute | ... | Pass/Fail |
| TC-004 | FR-004 | Generate optimized route using AI | 1. Admin selects route and clicks "Optimize" | Route generated within 10 seconds | ... | Pass/Fail |
| TC-005 | FR-005 | Driver views assigned route | 1. Driver logs in <br> 2. Opens dashboard | Daily route and student list are displayed | ... | Pass/Fail |
| TC-006 | FR-006 | Driver updates shuttle status | 1. Driver selects status (e.g., "En Route") | Status visible to parents and admin dashboards instantly | ... | Pass/Fail |
| TC-007 | FR-007 | Admin views shuttle performance report | 1. Admin opens Reports <br> 2. Selects shuttle and date | Report with duration, delays, fuel appears | ... | Pass/Fail |
| TC-008 | FR-010 | Student registers and sets pickup/drop-off | 1. Open registration <br> 2. Fill in student and location info <br> 3. Submit | Info saved, editable by admin/parent | ... | Pass/Fail |

---

## 🚀 Non-Functional Test Scenarios

### ✅ NF-TC-001: Performance Test – Real-Time Updates

- **Test Type**: Performance  
- **Scenario**: Simulate 1,000 users viewing the shuttle location map concurrently.  
- **Expected Result**: All users receive location updates within 5 seconds.  
- **Tool/Note**: Use load testing tool (e.g., JMeter or BlazeMeter) to simulate traffic.

---

### ✅ NF-TC-002: Security Test – Unauthorized Access Attempt

- **Test Type**: Security  
- **Scenario**: Attempt to access the admin dashboard without authentication (e.g., expired token or incorrect role).  
- **Expected Result**: Access denied, system logs unauthorized access attempt.  
- **Security Mechanism**: JWT authentication and role-based access control (RBAC)

---

> ✅ These test cases help validate both system behavior and robustness under real-world conditions.
