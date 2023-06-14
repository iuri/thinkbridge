# thinkbridge
Thinkbridge python challenge

This is a Flask application that provides an API for processing CSV files and saving them to Amazon S3.

## Prerequisites

- Python 3.x
- requests 2.26.0
- boto3 1.19.9
- beautifulsoup4 4.10.0
- pandas 1.3.3
- python-linkedin 0.4.1
- Flask 2.1.1
- template-render 0.1.0
## Installation

1. Clone the repository:

    '''' git  clone https://github.com/iuri/thinkbridge ''''


2. Navigate to the project directory:

    ''''cd thinkbridge''''

3. Install the required dependencies:

    ''''pip install -r requirements.txt''''

4. Create a file named as config.py in the root directory of the application:

    ''''touch config.py''''

- Edit the file and add the following environment/global variables:

    ''''
    \# Amazon S3 credentials

    S3_BUCKET = 'your-s3-bucket-name'

    S3_ACCESS_KEY = 'your-access-key'

    S3_SECRET_KEY = 'your-secret-key'

    \# LinkedIn S3 credentials

    LINKEDIN_USERNAME = 'your-username'

    LINKEDIN_PASSWORD = 'your-password'

    LINKEDIN_LOGIN_URL = 'linkedin-url'
    ''''
5. Set up Amazon S3:

- Create an S3 bucket on Amazon Web Services.
- Update the S3 bucket name, access key, and secret key in the Flask app code (`app.py`).

## Usage

1. Start the Flask server:

    ''''python3 app.py''''


2. Open your web browser and go to `http://localhost:5000`.

3. You will see a form where you can upload a CSV file.

4. Select a CSV file and click the "Upload" button.

5. The application will process the CSV file, generate a new processed CSV file, and upload it to the specified S3 bucket.

6. Once the file is uploaded, the application will display a success message along with the local file saved in the current directory, plus the file must be successfully saved in the AWS S3 instance.


<img width="1438" alt="Screen Shot 2023-06-14 at 5 33 10 PM" src="https://github.com/iuri/thinkbridge/assets/630005/204a694d-e585-4941-a64d-08db04c46845">




## License

This project is licensed under the [GPL License](LICENSE).

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [pandas](https://pandas.pydata.org/)
- [beautifulSoup4] (https://pypi.org/project/beautifulsoup4/)
- [python-linkedin] (https://pypi.org/project/python-linkedin/)
- [template-render] (https://pypi.org/project/template-render/)



## Initial Specification
Please find below the coding assignment, as part of your technical evaluation. We understand that a proper solution would take days, but please remember, a perfect solution doesn't exist.
We understand that this requires a frontend-backend solution. As a backend developer, your job will be to provide the backend solution. Use minimal frontend to supplement your backend solution if needed.
1. Requirements:

1.1 Give a CSV file of company names, create a python module that can find LinkedIn URLs for those companies. The LinkedIn URLs should be stored as a CSV file. And once that is done, extend the script using Playwright browser to find the employee count from LinkedIn and store it in the original file alongside the Company Names.

1.2. Use any csv reader you want and any scraper you want to accomplish this.

1.3. The module entry point can be a POST API endpoint that accepts csv files and returns the file with company name and employee count or a CLI program.


2. Please ensure the following points as well: 

    2.1. All API calls should be asynchronous.

    2.2 Include data validations wherever needed for all endpoints taking
inputs.

3. Exception handling needs to be present wherever applicable.
