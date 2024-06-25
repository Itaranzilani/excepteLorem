class NavSystem:
    def __init__(self):
        self.RequestFinished = Event()  # Create an event for RequestFinished

    def RequestFinishedCallback(self, request_result):
        # Handle the request result here
        pass

    def HandleOnRequestFinished(self):
        # Handle any logic or actions when a request is finished
        pass

# Create an instance of NavSystem
nav_system = NavSystem()

# Add the HandleOnRequestFinished function to the RequestFinished event
nav_system.RequestFinished += nav_system.HandleOnRequestFinished
