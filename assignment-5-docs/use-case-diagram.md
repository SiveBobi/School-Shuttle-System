
# 🧩 Use Case Diagram (GitHub-Compatible)

```mermaid
graph TD;
  %% Define Actors
  Passenger["Passenger"]:::actor
  Parent["Parent"]:::actor
  Driver["Driver"]:::actor
  Admin["Admin"]:::actor
  System["System"]:::actor
  Inspector["Traffic Inspector"]:::actor

  %% Passenger Use Cases
  Passenger -->|Requests| UC1["Book Shuttle"]
  Passenger -->|Views| UC2["View Shuttle Schedule"]
  Passenger -->|Cancels| UC3["Cancel Booking"]
  Passenger -->|Receives| UC4["Booking Confirmation"]
  Passenger -->|Tracks| UC5["Live Shuttle Tracking"]
  Passenger -->|Rates| UC6["Rate Shuttle Experience"]

  %% Parent Use Cases
  Parent -->|Tracks| UC5
  Parent -->|Receives Alerts| UC7["Receive Shuttle Alerts"]
  Parent -->|Manages Bookings| UC8["Manage Child Booking"]

  %% Driver Use Cases
  Driver -->|Views| UC9["View Assigned Routes"]
  Driver -->|Updates| UC10["Update Route Status"]
  Driver -->|Reports| UC11["Report Shuttle Issues"]
  Driver -->|Receives| UC12["Receive Passenger Info"]
  Driver -->|Logs| UC13["Log Driving Hours"]

  %% Admin Use Cases
  Admin -->|Manages| UC14["Manage Shuttle Fleet"]
  Admin -->|Assigns| UC15["Assign Drivers to Routes"]
  Admin -->|Monitors| UC16["Monitor System Performance"]
  Admin -->|Handles| UC17["Handle Complaints"]
  Admin -->|Generates| UC18["Generate Reports"]
  Admin -->|Updates| UC19["Update Shuttle Schedule"]

  %% Inspector Use Cases
  Inspector -->|Checks| UC20["Verify Shuttle Compliance"]
  Inspector -->|Reports| UC21["Report Safety Violations"]

  %% System Use Cases
  System -->|Sends| UC7
  System -->|Processes| UC4
  System -->|Stores| UC18
  System -->|Handles| UC17

  %% Styling
  classDef actor fill:#f9f,stroke:#333,stroke-width:1px;
  class Passenger,Parent,Driver,Admin,Inspector,System actor;














