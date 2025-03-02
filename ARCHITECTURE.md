```mermaid
%% === Level 1: System Context Diagram ===
graph TD;
  A[Student/Parent] -->|Uses| B[Mobile App];
  C[Driver] -->|Updates Shuttle Status| B;
  D[School Admin] -->|Manages System| E[Web Dashboard];
  B -->|Requests Data| F[Backend Server];
  E -->|Requests Data| F;
  F -->|Stores Data| G[Database];
  F -->|Fetches GPS Data| H[GPS API];
  F -->|Sends Notifications| I[Firebase Cloud Messaging];

%% === Level 2: Container Diagram ===
subgraph Web & Mobile Applications
    B
end

subgraph Admin Dashboard
    E
end

subgraph Backend Services
    F -->|Stores Route Data| G;
    F -->|Fetches GPS Data| H;
    F -->|Sends Notifications| I;
end

%% === Level 3: Component Diagram ===
subgraph Backend Components
    J[Authentication Service] -->|Authenticates Users| F;
    K[GPS Tracking Module] -->|Processes GPS Data| H;
    L[Route Optimization Engine] -->|Optimizes Routes| G;
    M[Notification System] -->|Sends Alerts| I;
end

F -->|Uses| J;
F -->|Calls| K;
F -->|Optimizes| L;
F -->|Sends Messages| M;

