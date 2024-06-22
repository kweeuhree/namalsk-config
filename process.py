import json

# Function to process locations and write new locations to a file
def process_coordinates(locations_object):
    # initialize result dictionary
    result = {"Triggers": []}

    # loop through locations object
    for location in locations_object['locations']:
       # extract minimum and maximum coordinates
        min_coords = location['min']
        max_coords = location['max']

        # calculate sizes and positions based on min and max coordinates
        sizes = [((max_coords[i] - min_coords[i])/2) for i in range(len(min_coords))]
        positions = [min_coords[i] + sizes[i] for i in range(len(min_coords))]

        # create a new location dictionary with required fields
        new_location = {
            "_Name": location['name'],
            "Position": positions,
            # orientation is always 0
            "Orientation": [0, 0, 0],
            "Size": sizes,
            "EyeAccommodation": location.get('darkness', 0),
            "Breadcrumbs": []
        }
        # append the new location to the result list
        result["Triggers"].append(new_location)
    
    # format the result dictionary as a JSON string with indentation
    formatted_output = json.dumps(result, indent=4)
    # write the formatted JSON string to a file
    with open('processed_coordinates.json', 'w') as file:
        file.write(formatted_output)
    # return the formatted JSON string
    return formatted_output


# Function to read JSON data from a file
def read_locations_from_file(filename):
    # open the specified file in read mode
    with open(filename, 'r') as file:
        # load the JSON data from the file
        data = json.load(file)
    # return data
    return data


# Main function
if __name__ == "__main__":
    # Read the locations object from a file
    locations_object = read_locations_from_file('locations.json') 

    # Process the coordinates and print the output
    formatted_output = process_coordinates(locations_object)
    print(formatted_output) #<---- comment out if you dont want console output