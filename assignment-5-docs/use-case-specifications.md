
# 📄 Use Case Specifications

This document provides detailed specifications for 8 critical use cases of the **School Shuttle Management System**.

---

### ✅ Use Case 1: View Real-Time Shuttle Location

- **Actor(s)**: Parent, Student  
- **Description**: Allows users to view the shuttle’s live location on a map.
- **Preconditions**: User is logged into the mobile app.
- **Postconditions**: Shuttle location pin is updated every 5 seconds on the map.

**Basic Flow:**
1. User logs in and opens the map screen.
2. System retrieves the latest GPS location of the shuttle.
3. System displays the shuttle’s current position on the map.
4. Map auto-refreshes every 5 seconds.

**Alternative Flows:**
- GPS signal is lost → System shows “Location unavailable” message.

---

### ✅ Use Case 2: Receive Notifications (Approaching Location)

- **Actor(s)**: Parent  
- **Description**: Sends automatic notification when the shuttle is approaching the pickup/drop-off location.
- **Preconditions**: Default pickup/drop-off location is saved.
- **Postconditions**: Parent receives a push notification.

**Basic Flow:**
1. Shuttle enters 500-meter radius of student location.
2. System detects proximity.
3. System sends push notification to the parent.

**Alternative Flows:**
- Notification service fails → Parent receives SMS as backup (if enabled).

---

### ✅ Use Case 3: Manage Shuttle Routes

- **Actor(s)**: Admin  
- **Description**: Allows admin to add, edit, or delete shuttle routes.
- **Preconditions**: Admin is logged into dashboard.
- **Postconditions**: Routes are updated across all systems.

**Basic Flow:**
1. Admin navigates to Routes panel.
2. Admin adds or updates route details.
3. System saves changes and refreshes map data.

**Alternative Flows:**
- Invalid route details → System prompts for correction.

---

### ✅ Use Case 4: Optimize Routes Using AI

- **Actor(s)**: Admin  
- **Description**: Uses AI to calculate the most efficient shuttle route.
- **Preconditions**: Admin selects routes to optimize.
- **Postconditions**: Optimized route is generated and viewable.

**Basic Flow:**
1. Admin selects "Optimize Route."
2. System processes all routes using AI.
3. Optimized route is generated within 10 seconds.

**Alternative Flows:**
- AI fails to process → Admin is prompted to try again.

---

### ✅ Use Case 5: View Assigned Routes

- **Actor(s)**: Driver  
- **Description**: Allows driver to view their daily assigned shuttle route and student list.
- **Preconditions**: Driver is logged into the system.
- **Postconditions**: Driver dashboard displays correct route info.

**Basic Flow:**
1. Driver logs in.
2. System fetches today's assigned route.
3. Route details and student pickup list are displayed.

**Alternative Flows:**
- No route assigned → System shows “No assignment available” message.

---

### ✅ Use Case 6: Update Shuttle Status

- **Actor(s)**: Driver  
- **Description**: Driver updates the current status of the shuttle (e.g., En Route, Arrived, Delayed).
- **Preconditions**: Driver is logged in.
- **Postconditions**: Status is updated in real time for all users.

**Basic Flow:**
1. Driver selects a status from the dashboard.
2. System records the status.
3. Parents and admin dashboards reflect the new status.

**Alternative Flows:**
- Network error → System retries or stores update offline.

---

### ✅ Use Case 7: View Shuttle Performance Reports

- **Actor(s)**: Admin  
- **Description**: View analytics reports including trip duration, fuel usage, and delays.
- **Preconditions**: Admin is logged in.
- **Postconditions**: Reports are generated and viewable.

**Basic Flow:**
1. Admin navigates to Reports section.
2. Selects a date range and shuttle.
3. System displays performance metrics.

**Alternative Flows:**
- No data available → System shows “No data for selected range.”

---

### ✅ Use Case 8: Register and Set Pickup/Drop-off Location

- **Actor(s)**: Student, Parent  
- **Description**: Register for shuttle use and set preferred pickup/drop-off location.
- **Preconditions**: Student is not yet registered for shuttle.
- **Postconditions**: Location is saved and editable.

**Basic Flow:**
1. User selects "Register for Shuttle."
2. Enters personal and location details.
3. System saves the student info and assigned route.

**Alternative Flows:**
- Invalid location → System prompts for correction.

