
# Database Security Testing Tool

## Overview
This tool is designed to proactively identify security gaps and vulnerabilities in databases, with capabilities for threat modeling and vulnerability scoring. It supports MySQL and PostgreSQL databases, with planned support for SQL Server, S3, and Redshift.

## Features
- **Advanced Vulnerability Scanning**: Checks for weak password policies, privilege escalation risks, SSL/TLS configurations, and public access exposure.
- **Threat Modeling Integration**: Maps vulnerabilities to MITRE ATT&CK tactics and provides scenario-based threat models.
- **Risk Scoring and Reporting**: Generates detailed reports with risk scores, recommendations, and remediation guidance.
- **Modular Design**: Easily expand with additional checks, plugins, and database configurations.

## Requirements
- **Python 3.8+**
- Install dependencies using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/database-security-testing-tool.git
    cd database-security-testing-tool
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Database Settings**:
    - Open `config.json` and set up database connection details for MySQL, PostgreSQL, and any other databases you want to connect to in future updates.

## Usage
1. **Run Vulnerability Scanner**:
    ```bash
    python vulnerability_scanner.py
    ```
   - The scanner will check for weak passwords, privilege escalation risks, SSL/TLS configuration, and public access exposure.

2. **Generate Vulnerability Report**:
    ```bash
    python vulnerability_report.py
    ```
   - Generates reports with risk scores and recommendations in `vulnerability_report.txt` (plaintext) and `vulnerability_report.json` (JSON).

## Configuration
- **config.json**: Central configuration for database connection details.
    - **MySQL and PostgreSQL Settings**: Define host, user, password, and database names.
    - Future support for SQL Server, S3, and Redshift can be added here.

## Advanced Features
1. **Threat Modeling and MITRE Mapping**:
   - The tool maps identified vulnerabilities to MITRE ATT&CK tactics to provide context for red teaming and incident response.

2. **Risk Scoring**:
   - Each vulnerability is scored based on severity and exploitability, helping prioritize critical issues.

3. **Modular Design**:
   - To extend functionality, add custom checks or compliance benchmarks by modifying `vulnerability_scanner.py` or adding new plugins.

## Example Configuration and Sample Output
- **config.json** (Example):
    ```json
    {
        "mysql": {
            "host": "localhost",
            "user": "root",
            "password": "password",
            "database": "testdb"
        },
        "postgresql": {
            "host": "localhost",
            "user": "postgres",
            "password": "password",
            "database": "testdb"
        }
    }
    ```

- **Sample Output (vulnerability_report.txt)**:
    ```
    Database Vulnerability Report
    ===========================
    Total Vulnerabilities: 3
    Total Risk Score: 22

    Description: Weak password detected for user 'admin'.
    Severity: High
    Risk Score: 21
    MITRE ATT&CK Tactic: TA0001 - Initial Access
    Recommendation: Enforce strong password policies with minimum complexity and length requirements.
    ```

## License
This project is licensed under the MIT License.

## Support
For issues or support, please open an issue on the GitHub repository.
