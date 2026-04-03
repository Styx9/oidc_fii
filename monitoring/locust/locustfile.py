from locust import HttpUser, task, between

class CloudPulseUser(HttpUser):
    # Simulate a user waiting between 1 and 5 seconds between clicks
    host = "http://10.0.0.10"
    wait_time = between(1, 5)

    @task(3)
    def view_index(self):
        """Simulate viewing the main page"""
        self.client.get("/")

    @task(1)
    def view_image(self):
        """Simulate loading the background image from S3 via the Flask proxy"""
        self.client.get("/background-image")

    @task(1)
    def trigger_error(self):
        """Optional: hit a non-existent page to generate 404s in Loki logs"""
        self.client.get("/not-found", name="/not-found-test")