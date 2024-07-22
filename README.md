# openfeature_withharnesssdk

OpenFeature Python Integration with Harness

This project demonstrates the integration of the OpenFeature framework with Harness, a feature management tool, using Django. 
The aim is to provide a streamlined approach to managing feature flags within a Python application, enabling dynamic feature control and A/B testing capabilities.

Key Components:

Django Framework: Serves as the web framework to handle HTTP requests and responses.
OpenFeature: An open standard for feature flag management, offering a unified Evaluation API and Providers to interact with various feature flag providers in this project now i can fetch the features flag value for , boolean flag, and multivariate flag(string_variation, integer_variation, and object_variation from the harness feature flag management service using open feature python sdk integration.
Harness: A powerful feature management tool used to manage feature flags and control feature releases.

Project Structure:

providers.py: Contains the HarnessClient class to initialize and manage the connection with Harness, and methods to evaluate feature flags.
services.py: Defines the FeatureFlagService class, leveraging HarnessClient to fetch the status of feature flags.
views.py: Implements the FeatureFlagController class to handle HTTP GET requests, retrieving the feature flag status and returning it as a JSON response.
i have implemented the feature flag connection with harness client to get the string value for the multivariant feature flag.

urls.py: Configures the URL routing to map the endpoint to the corresponding view.

Usage:

Start the Django server.
Access the feature flag status via the endpoint: localhost:feature/openfeature?flag_name=<flag_name>
for string variation :localhost:/feature/user6@rinet.com/
for integer :localhost:/feature/integer?flag_name=multivariant_number
for object : localhost:/feature/object?flag_name=json_object_variation




This setup allows real-time feature flag evaluation, facilitating dynamic control over feature visibility in the application.

i have implemented the test case for feature flag evaluation for all the providers methods that is : resolve_boolean_details,resolve_string_details ,resolve_integer_details and resolve_object_details.

you can also run the test by running the following command:
python manage.py test feature_app.tests 