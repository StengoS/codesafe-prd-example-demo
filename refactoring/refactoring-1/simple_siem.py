import time

class SimpleSIEM:
    def __init__(self):
        # In-memory log storage
        self.logs = []  
    
    def get_version_info(self):
        print("Simple SIEM v0.01")

    def ingest_log(self, log):
        # Simulate log ingestion
        self.logs.append(log)
        print(f"Ingested log: {log}")

    def query_logs(self, keyword):
        # Simulate log querying
        results = [log for log in self.logs if keyword in log]
        print(f"Query results for '{keyword}': {results}")
        return results

# Example usage
"""
siem = SimpleSIEM()
siem.ingest_log("ERROR: Failed to authenticate user")
siem.ingest_log("INFO: User logged in")
siem.ingest_log("WARNING: Disk usage above 80%")

siem.query_logs("ERROR")  # Query for ERROR logs
siem.query_logs("User")   # Query for logs containing "User"
"""