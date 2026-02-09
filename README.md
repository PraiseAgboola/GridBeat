# GridHeartbeat Nigeria System Documentation

## Overview
GridHeartbeat is a robust system designed to monitor and report the operational status of grid infrastructures in Nigeria, enabling stakeholders to make informed decisions regarding grid management and maintenance.

## Architecture Overview
The GridHeartbeat system is composed of several key components:
1. **Data Aggregator**: Collects data from various grid points.
2. **Data Processor**: Analyzes the collected data to identify trends and anomalies.
3. **User Interface**: A web-based interface for users to visualize data and generate reports.
4. **Database**: Stores the historical data for retrieval and analysis.
5. **API**: Enables communication between the frontend and the backend services.

## Setup Instructions
1. **Prerequisites**:
   - Node.js (version 14 or higher)
   - MongoDB (version 4.0 or higher)
   
2. **Clone the repository**:
   ```bash
   git clone https://github.com/PraiseAgboola/GridBeat.git
   cd GridBeat
   ```

3. **Install dependencies**:
   ```bash
   npm install
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and set the necessary variables based on the `.env.example` file.

5. **Run the Application**:
   ```bash
   npm start
   ```

## Deployment Guide
To deploy the GridHeartbeat system, follow these steps:
1. **Prepare the Server**:
   - Ensure that the server meets the system requirements.
   - Install necessary software (Node.js, MongoDB).

2. **Clone the Repository on the Server**:
   ```bash
   git clone https://github.com/PraiseAgboola/GridBeat.git
   cd GridBeat
   ```

3. **Install Dependencies**:
   ```bash
   npm install
   ```

4. **Set Environment Variables** and ensure they match your production settings.

5. **Start the Application**:
   You can start the application in the background using PM2 or similar process managers:
   ```bash
   pm2 start server.js
   ```

## Conclusion
This documentation provides a comprehensive overview of the GridHeartbeat system. For further inquiries or contributions, please reach out to the repository owner or the project collaborators.