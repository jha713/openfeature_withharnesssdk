# openfeature_withharnesssdk

OpenFeature Python Integration with Harness
This project demonstrates the integration of the OpenFeature framework with Harness, a feature management tool, using Django. The aim is to provide a streamlined approach to managing feature flags within a Python application, enabling dynamic feature control and A/B testing capabilities.

Key Components:

Django Framework: Serves as the web framework to handle HTTP requests and responses.
OpenFeature: An open standard for feature flag management, offering a unified API to interact with various feature flag providers.
Harness: A powerful feature management tool used to manage feature flags and control feature releases.
Project Structure:

providers.py: Contains the HarnessClient class to initialize and manage the connection with Harness, and methods to evaluate feature flags.
services.py: Defines the FeatureFlagService class, leveraging HarnessClient to fetch the status of feature flags.
views.py: Implements the FeatureFlagController class to handle HTTP GET requests, retrieving the feature flag status and returning it as a JSON response.
urls.py: Configures the URL routing to map the endpoint to the corresponding view.
Usage:

Start the Django server.
Access the feature flag status via the endpoint: http://127.0.0.1:8081/feature/openfeature?flag_name=<flag_name>
