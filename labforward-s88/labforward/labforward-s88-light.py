import http.client  # Provides an HTTP client for interacting with APIs.
import urllib.parse  # Provides functions for parsing URLs and encoding query strings.
import base64  # Provides functions for encoding and decoding binary data as base64.
import json  # Provides functions for working with JSON data.
import xml.etree.ElementTree as ET  # Provides an XML parsing library.
import xml.dom.minidom as minidom  # Provides a library for manipulating XML documents.
import pandas as pd  # Provides a data manipulation library.
from datetime import datetime  # Provides functions for working with dates and times.
from xml.etree.ElementTree import Element, SubElement, Comment, tostring  # Provides classes for creating and manipulating XML data.
import os
from dotenv import load_dotenv

#This module contains functions for interacting with an external API, manipulating XML data, and converting it to a pandas DataFrame.


# Get the directory where this .env  is located
def load_all_env_files(directory="."):
    """
    Load all .env files found in the specified directory.

    Parameters:
        directory (str): The directory where .env files will be searched. Default is the current directory.

    Returns:
        None
    """
    # Get a list of all files in the specified directory
    files = os.listdir(directory)

    # Filter the list to include only .env files
    env_files = [file for file in files if file.endswith(".env")]

    # Load environment variables from each .env file
    for env_file in env_files:
        dotenv_path = os.path.join(directory, env_file)
        load_dotenv(dotenv_path)

# Usage:
# Load all .env files from the current directory
load_all_env_files()



#This code defines the URL for the OAuth 2.0 server and the client credentials needed toauthenticate with the server.
oauth_url = "laboperator.labforward.app"  # The URL of the OAuth 2.0 server.
# Access environment variables
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

def get_new_token(oauth_url, client_id, client_secret):
    """
    Retrieves a new access token from the OAuth 2.0 server using the provided client ID and client secret.

    Parameters:
        oauth_url (str): The URL of the OAuth 2.0 server.
        client_id (str): The client ID for your application.
        client_secret (str): The client secret for your application.

    Returns:
        str: The new access token.
    """
    # Set up a connection with the OAuth 2.0 server
    conn = http.client.HTTPSConnection(oauth_url)

    # Construct the necessary headers and data
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode('utf-8')
    }
    data = urllib.parse.urlencode({
        "grant_type": "client_credentials"
    })

    # Send the HTTP request and receive the response
    conn.request("POST", "/oauth/token", body=data, headers=headers)
    response = conn.getresponse()
    response_data = response.read()

    # Decode the response data to a string and extract the necessary information
    response_str = response_data.decode('utf-8')
    response_dict = json.loads(response_str)
    access_token = response_dict["access_token"]
    #print(access_token)
    return access_token



def get_workflow_run_data(workflow_run_id, oauth_url, client_id, client_secret):
    """
    Retrieves data for a specific Laboperator workflow run from the API and returns it as a pretty-printed JSON object.

    Parameters:
        workflow_run_id (str): The ID of the workflow run to retrieve data for.
        oauth_url (str): The URL of the OAuth 2.0 server.
        client_id (str): The client ID for your application.
        client_secret (str): The client secret for your application.

    Returns:
        str: The pretty-printed JSON object containing the data for the workflow run.
    """
    # Get a new access token
    access_token = get_new_token(oauth_url, client_id, client_secret)

    # Set up a connection to the API and construct the necessary headers and payload
    conn = http.client.HTTPSConnection(f"{oauth_url}")
    payload = ''
    headers = {
      'Accept': 'application/vnd.api+json',
      'Authorization': f'Bearer {access_token}'
    }

    # Send the HTTP request and receive the response
    conn.request("GET", f"/api/v2/labforward/workflow_runs/{workflow_run_id}?template=true", payload, headers)
    res = conn.getresponse()
    data = res.read()
    

    # Parse the JSON response into a dictionary object
    json_data = json.loads(data)

    # Pretty-print the JSON object
    pretty_json = json.dumps(json_data, indent=4)

    return pretty_json



def get_measurement_data(measurement_id, oauth_url, client_id, client_secret):
    """
    Retrieves measurement data for a specific Laboperator measurement from the API and returns it as a pretty-printed JSON object.

    Parameters:
        measurement_id (str): The ID of the measurement to retrieve data for.
        oauth_url (str): The URL of the OAuth 2.0 server.
        client_id (str): The client ID for your application.
        client_secret (str): The client secret for your application.

    Returns:
        str: The pretty-printed JSON object containing the data for the measurement.

    """
    # Define the fixed output file path
    output_file = "measurement_data.txt"
    # Get a new access token
    access_token = get_new_token(oauth_url, client_id, client_secret)

    # Set up a connection to the API and construct the necessary headers and payload
    conn = http.client.HTTPSConnection(f"{oauth_url}")
    payload = ''
    headers = {
      'Accept': 'application/vnd.api+json',
      'Authorization': f'Bearer {access_token}'
      }

    # Send the HTTP request and receive the response
    conn.request("GET", f"/api/v2/Bayer/measurements/{measurement_id}?data_points=true&locale=en", payload, headers)
    res = conn.getresponse()
    data = res.read()

    # Decode the response data to a string and extract the necessary information
    response_str = data.decode('utf-8')

    # Parse the JSON response into a dictionary object
    json_data = json.loads(response_str)

    # Pretty-print the JSON object
    pretty_json = json.dumps(json_data, indent=4)

        # Save the data to the fixed output file
    #with open(output_file, 'w', encoding='utf-8') as f:
        # Write the "pretty-printed" JSON data to the file
      #  pretty_json = json.dumps(json.loads(response_str), indent=4)
     #   f.write(pretty_json)

    #print(f"Measurement data saved to {output_file}")
    
    return pretty_json


def remove_line_breaks(d):
    """
    Recursively removes line breaks from the values of a dictionary.

    Parameters:
        d (dict): The dictionary to remove line breaks from.

    Returns:
        None.
    """
    for k, v in d.items():
        if isinstance(v, dict):
            # If the value is a dictionary, call the function recursively.
            remove_line_breaks(v)
        elif isinstance(v, str):
            # If the value is a string, replace any line breaks with spaces.
            d[k] = v.replace('\n', ' ')
        elif isinstance(v, list):
            # If the value is a list, iterate over each element and call the function recursively if necessary.
            for i, val in enumerate(v):
                if isinstance(val, dict):
                    remove_line_breaks(val)
                elif isinstance(val, str):
                    v[i] = val.replace('\n', ' ')



def dict_to_element(tag, d):
    """
    Converts a dictionary to an XML element with the specified tag.

    Parameters:
        tag (str): The tag for the XML element.
        d (dict): The dictionary to convert to an XML element.

    Returns:
        xml.etree.ElementTree.Element: The XML element.
    """
    elem = ET.Element(tag)
    for key, value in d.items():
        if isinstance(value, dict):
            # If the value is a dictionary, call the function recursively.
            child_elem = dict_to_element(key, value)
            elem.append(child_elem)
        elif isinstance(value, list):
            # If the value is a list, iterate over each element and call the function recursively if necessary.
            for item in value:
                if isinstance(item, dict):
                    child_elem = dict_to_element(key, item)
                    elem.append(child_elem)
                else:
                    # If the item is not a dictionary, create a new element and set its text to the item value.
                    item_elem = ET.Element(key)
                    item_elem.text = str(item)
                    elem.append(item_elem)
        else:
            # If the value is neither a dictionary nor a list, set the element's attribute to the value.
            elem.set(key, str(value))
    
    return elem


def add_data_points_to_element(root_element, data_points_dict, trends_node_name):
    """
    Adds data points to an XML element.

    Parameters:
        root_element (xml.etree.ElementTree.Element): The root element to add the data points to.
        data_points_dict (dict): A dictionary containing the data points to add.
        trends_node_name (str): The name of the Trends node to add the data points to.

    Returns:
        xml.etree.ElementTree.Element: The updated root element.
    """
    # Find or create the Trends node
    trends_node = root_element.find(trends_node_name)
    if trends_node is None:
        trends_node = ET.Element(trends_node_name)
        root_element.append(trends_node)

    # Check if there are data points
    if 'data_points' in data_points_dict and data_points_dict['data_points']:
        # Create a new Trend node and add the data points to it
        trend_node = ET.SubElement(trends_node, "Trend", {"Name": data_points_dict['name'], "Unit": data_points_dict['unit']})

        # Find the earliest timestamp and calculate the time offset
        timestamps = [data_point[1] for data_point in data_points_dict['data_points']]
        min_timestamp = min(timestamps)
        time_offset = datetime.strptime(min_timestamp, '%Y-%m-%dT%H:%M:%S.%fZ') - datetime.min

        # Sort the data points in ascending order based on the timestamp
        sorted_data_points = sorted(data_points_dict['data_points'], key=lambda x: x[1])

        # Add the data points to the Trend node as V nodes with relative timestamps
        for data_point in sorted_data_points:
            timestamp_str = data_point[1]
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            rel_time_str = str(timestamp - datetime.min - time_offset).split('.')[0]  # hh:mm:ss format
            value = data_point[2]

            # Create a new "V" node for the data point and add it to the Trend node
            value_node = ET.SubElement(trend_node, "V", {"T": rel_time_str})
            value_node.text = str(value)

    return root_element


def format_seconds(seconds):
    """
    Format the given number of seconds as a time value in the "hh:mm:ss" format.

    Parameters:
        seconds (float): The number of seconds to format.

    Returns:
        str: The formatted time value.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"


def build_xml(workflow_run_id, measurement_ids, xml_filename):
    """
    Builds an XML file containing data from a Laboperator workflow run and associated measurements.

    Parameters:
        workflow_run_id (int): The ID of the workflow run to extract data from.
        measurement_ids (list): A list of measurement IDs to extract data from.
        xml_filename (str): The name of the output XML file.

    Returns:
        None.
    """
    # Get the workflow run data 
    workflow_run_data = get_workflow_run_data(workflow_run_id, oauth_url, client_id, client_secret)

    # Convert the workflow run data to a dictionary and remove line breaks
    workflow_run_dict = json.loads(workflow_run_data)
    remove_line_breaks(workflow_run_dict)

    # Create the Experiment root element
    experiment_elem = ET.Element("Experiment")

    # Add the workflow run data as a child of Experiment
    workflow_run_elem = dict_to_element("workflow_run_dict", workflow_run_dict)
    experiment_elem.append(workflow_run_elem)

    # Loop through each measurement ID and add a new Trend for each one
    for measurement_id in measurement_ids:
        # Get the measurement data
        measurement_data = get_measurement_data(measurement_id, oauth_url, client_id, client_secret)

        # Convert the measurement data to a dictionary
        measurement_dict = json.loads(measurement_data)

        # Check if the necessary keys exist before proceeding
        if "data" in measurement_dict and "attributes" in measurement_dict["data"]:
            data_points = measurement_dict["data"]["attributes"].get("data_points", [])
            if data_points:
                # Create a new Trend element for this measurement
                trend_node = ET.Element("Trend", {"name": measurement_dict["data"]["id"]})
                experiment_elem.append(trend_node)

                # Organize data points by channel ID
                data_points_by_channel = {}
                min_timestamps_by_channel = {}  # Store the minimum timestamps for each channel

                for data_point in data_points:
                    channel_id = data_point[0]
                    timestamp = data_point[1]
                    value = data_point[2]

                    if channel_id not in data_points_by_channel:
                        data_points_by_channel[channel_id] = []

                    data_points_by_channel[channel_id].append((timestamp, value))

                    # Calculate the minimum timestamp for each channel
                    if channel_id not in min_timestamps_by_channel:
                        min_timestamps_by_channel[channel_id] = timestamp
                    else:
                        min_timestamps_by_channel[channel_id] = min(
                            min_timestamps_by_channel[channel_id], timestamp
                        )

                # Create a Data element to hold channel data points
                data_elem = ET.Element("Data")
                trend_node.append(data_elem)

                # Loop through channels and add data points
                for channel_id, channel_data_points in data_points_by_channel.items():
                    # Skip channels with no data points
                    if not channel_data_points:
                        continue

                    # Sort data points within each channel by timestamp
                    channel_data_points.sort(key=lambda x: x[0])

                    channel_elem = ET.Element("Channel", {"id": str(channel_id)})
                    data_elem.append(channel_elem)

                    # Get the minimum timestamp for this channel
                    min_timestamp = min_timestamps_by_channel[channel_id]
                    min_timestamp_datetime = datetime.strptime(
                        min_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ"
                    )

                    for timestamp, value in channel_data_points:
                        # Parse the timestamp string into a datetime object
                        timestamp_datetime = datetime.strptime(
                            timestamp, "%Y-%m-%dT%H:%M:%S.%fZ"
                        )

                        # Calculate the relative timestamp as a floating-point number
                        relative_timestamp_seconds = (
                            timestamp_datetime - min_timestamp_datetime
                        ).total_seconds()

                        # Format the relative timestamp as a time value
                        relative_timestamp = format_seconds(relative_timestamp_seconds)

                        data_point_elem = ET.Element(
                            "DataPoint", {"timestamp": relative_timestamp}
                        )
                        data_point_elem.text = str(value)
                        channel_elem.append(data_point_elem)


    # Create the XML string from the Experiment element
    xml_string = ET.tostring(experiment_elem, encoding='utf-8')
    xml_pretty_string = minidom.parseString(xml_string).toprettyxml(indent='  ')

    # Write the XML string to a file
    with open(xml_filename, 'w') as f:
        f.write(xml_pretty_string)

    # Print a message confirming the file was saved
    print(f'File saved to {xml_filename}')

def build_dataframe(workflow_run_id, measurement_ids, output_csv_filename):
    """
    Extracts data from a Laboperator workflow run and associated measurements and saves it to a CSV file.

    Parameters:
        workflow_run_id (int): The ID of the workflow run to extract data from.
        measurement_ids (list): A list of measurement IDs to extract data from.
        output_csv_filename (str): The name of the output CSV file.

    Returns:
        None
    """
    # Create an empty list to store DataFrames
    df_list = []

    # Get the workflow run data
    workflow_run_data = get_workflow_run_data(workflow_run_id, oauth_url, client_id, client_secret)

    # Convert the workflow run data to a dictionary and remove line breaks
    workflow_run_dict = json.loads(workflow_run_data)
    remove_line_breaks(workflow_run_dict)

    # Loop through each measurement ID
    for measurement_id in measurement_ids:
        # Get the measurement data
        measurement_data = get_measurement_data(measurement_id, oauth_url, client_id, client_secret)

        # Convert the measurement data to a dictionary
        measurement_dict = json.loads(measurement_data)

        # Check if the necessary keys exist before proceeding
        if "data" in measurement_dict and "attributes" in measurement_dict["data"]:
            data_points = measurement_dict["data"]["attributes"].get("data_points", [])
            if data_points:
                # Create a DataFrame for this measurement's data
                measurement_df = pd.DataFrame(data_points, columns=["channel_id", "timestamp", "value"])

                # Convert timestamp strings to datetime objects
                measurement_df["timestamp"] = pd.to_datetime(measurement_df["timestamp"])

                # Calculate the minimum timestamp for this measurement
                min_timestamp = measurement_df["timestamp"].min()

                # Calculate relative timestamps as timedelta objects
                measurement_df["relative_timestamp"] = (measurement_df["timestamp"] - min_timestamp)

                # Add a column for the measurement ID
                measurement_df["measurement_id"] = measurement_dict["data"]["id"]

                # Append the measurement DataFrame to the list
                df_list.append(measurement_df)

    # Concatenate all DataFrames in the list
    result_df = pd.concat(df_list, ignore_index=True)

    # Format relative timestamps as hh:mm:ss strings
    result_df["relative_timestamp"] = result_df["relative_timestamp"].apply(lambda x: str(x).split()[2])

    # Save the DataFrame to a CSV file
    result_df.to_csv(output_csv_filename, index=False)

    print(f"DataFrame saved to {output_csv_filename}")



#build_xml(workflow_run_id, measurement_id, r"C:\Users\Peter Dinh\Desktop\S88packackage\api-test3.xml")
#build_dataframe(workflow_run_id, measurement_id, r"C:\Users\Peter Dinh\Desktop\S88packackage\api-test-df3.csv")