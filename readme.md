<p>Script for a DayZ mod that ultimately allows configuration or addition of darkness areas using Namalsk's darkness system.</p>
<p>My script enables easy conversion between two different coordinate systems:</p>
<code>

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
</code>

<p>Original solution involved multiple for loops, which worked, but considering the need to process large amounts of data, list comprehensions were a better choice. List comprehensions are generally faster than for loops because they are optimmized for creating lists in Python.</p>

<p>The resultant object is formatted and written to a file:</p>
<code>

    # format the result dictionary as a JSON string with indentation
    formatted_output = json.dumps(result, indent=4)
    # write the formatted JSON string to a file
    with open('processed_coordinates.json', 'w') as file:
        file.write(formatted_output)

</code>

<p>Overall, this script reads location data from a JSON file, processes the coordinates to convert to specified fields, writes the processed data to a new JSON file (processed_coordinates.json), and optionally prints the formatted JSON string to the console for verification or debugging purposes.</p>
