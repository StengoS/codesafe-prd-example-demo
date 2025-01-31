class SimpleSIEM:
    def __init__(self):
        # In-memory log storage
        self.logs = []
    
    def get_version_info(self):
        print("Simple SIEM v0.02")

    # Simulate log ingestion
    def ingest_log(self, log):
        self.logs.append(log)
        print(f"Ingested log: {log}")

    # Simulate log querying
    def query_logs(self, keyword):
        results = [log for log in self.logs if keyword in log]
        return results
    
    # Send an alert if the amount of ERROR and CRITICAL logs above the threshold
    def check_errors_with_threshold(self):
        error_logs = self.query_logs("ERROR")
        critical_logs = self.query_logs("CRITICAL")

        total = len(error_logs) + len(critical_logs)

        if total >= 5:
            print("High amount of errors detected!")
        else:
            print("Amount of errors under set threshold.")


# Example usage
"""
siem = SimpleSIEM()
siem.ingest_log("ERROR: Failed to authenticate user")
siem.ingest_log("INFO: User logged in")
siem.ingest_log("WARNING: Disk usage above 80%")

siem.query_logs("ERROR")  # Query for ERROR logs
siem.query_logs("User")   # Query for logs containing "User"
"""