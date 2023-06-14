# https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
from flask import Flask, request
import boto3

import requests
from bs4 import BeautifulSoup

from linkedin_api import Linkedin
import pandas as pd

import config

app = Flask(__name__)


# Amazon S3 credentials
S3_BUCKET = config.S3_BUCKET
S3_ACCESS_KEY = config.S3_ACCESS_KEY
S3_SECRET_KEY = config.S3_SECRET_KEY

def save2S3(filename):
        
        # Save the processed DataFrame to a new CSV file
        processed_file_path = './' + filename

        # Upload the processed CSV file to Amazon S3
        s3 = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY)
        s3.upload_file(processed_file_path, S3_BUCKET, filename)

        # Return a success message with the S3 file URL
        s3_file_url = f'https://{S3_BUCKET}.s3.amazonaws.com/{new_filename}'
        return f'CSV file processed and saved to S3: {s3_file_url}', 200



def save2csv(data, filename):
    df = pd.DataFrame(data.items(), columns=['Company Name', 'LinkedIn URL'])
    df.to_csv(filename, index=False)


def get_linkedin_urls(company_names):
    # print(company_names)
    linkedin_urls = {}
    for company_name in company_names:
        try:
            # print(company_name)
            # Send a search query to LinkedIn
            search_url = f"https://www.linkedin.com/search/results/companies/?keywords={company_name}"
            response = requests.get(search_url)

            # Parse the HTML response
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the first search result
            first_result = soup.find('li', class_='reusable-search__result-container')

            # Extract the LinkedIn URL
            if first_result:
                linkedin_url = first_result.find('a')['href']
                linkedin_urls[company_name] = linkedin_url
            else:
                linkedin_url = 'https://default.com'                   
                linkedin_urls[company_name] = linkedin_url
            # print(linkedin_urls)
        except Exception as e:
            print(f"Error finding LinkedIn URL for {company_name}: {str(e)}")
        
    return linkedin_urls




def get_linkedin_urls2(company_names):

    # print(company_names)
    # Initialize the LinkedIn API client
    linkedin = Linkedin()

    # Create a dictionary to store the LinkedIn URLs
    linkedin_urls = {}

    # Iterate over the company names and find their LinkedIn URLs
    for company_name in company_names:
        try:
            # Search for the company on LinkedIn
            search_results = linkedin.search_entities(company_name)
            company_result = search_results.get('elements', [])[0]
            linkedin_url = company_result.get('targetUrn')

            # Store the LinkedIn URL in the dictionary
            linkedin_urls[company_name] = linkedin_url

        except Exception as e:
            print(f"Error finding LinkedIn URL for {company_name}: {str(e)}")

    return linkedin_urls





@app.route('/upload', methods=['POST'])
def process_csv():
    # print('request', request.files)
    # print(request.files['file'])
    # Check if file was sent in the request
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    # Check if the file has a CSV extension
    if not file.filename.endswith('.csv'):
        return 'Invalid file format. Only CSV files are allowed.', 400

    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file)

        # Perform your data processing operations on the DataFrame
        # For example, let's capitalize all the column names
        df.columns = df.columns.str.upper()
        # print(df)

        data = df.iloc[:, 0].tolist() 

        data = get_linkedin_urls(data)
        # print(urls)

        filename = 'linkedin_urls.csv'
        # save2S3(filename)
        save2csv(data, filename)

        

        return True
    except Exception as e:
        return f'Error processing the CSV file: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
