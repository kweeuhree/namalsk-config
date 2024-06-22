def process_coordinates(locations_object):
    result = {"triggers": []}

    for location in locations_object['locations']:
        min_coords = location['min']
        max_coords = location['max']

        sizes = [((max_coords[i] - min_coords[i])/2) for i in range(len(min_coords))]
        positions = [min_coords[i] + sizes[i] for i in range(len(min_coords))]

        new_location = {
            "_Name": location['name'],
            "Position": positions,
            "Orientation": [0, 0, 0],
            "Size": sizes,
            "EyeAccommodation": location.get('darkness', 0),
            "Breadcrumbs": []
        }

        result["triggers"].append(new_location)
    

    print(result)
    return result


# def process_coordinates(locations_object):
#     result = {"triggers": []}
    
#     for location in locations_object['locations']:
#         positions = []
#         sizes = []

#         # Calculate sizes
#         for i in range(len(location['min'])):
#             size = (location['max'][i] - location['min'][i])/2
#             sizes.append(size)

#         # Calculate positions
#         for i in range(len(location['min'])):
#             position = location['min'][i] + sizes[i]
#             positions.append(position)

#         # Construct new location object
#         new_location = {
#             "_Name": location['name'],
#             "Position": positions,
#             "Orientation": [0, 0, 0],
#             "Size": sizes,
#             "EyeAccommodation": location.get('darkness', 0),  # Assuming default darkness is 0 if not present
#             "Breadcrumbs": []
#         }

#         result["triggers"].append(new_location)

#     print(result)
#     return result


process_coordinates({
    "enabled": 1,
    "debugging": 0,
    "locations":
    [
        {
            "name": "Test1",
            "min": [
                10.0,
                0.0,
                10.0
            ],
            "max": [
                100.0,
                20.0,
                50.0
            ],
            "darkness": 0.3
        },
        {
            "name": "Test2",
            "min": [
                20.0,
                10.0,
                1.0
            ],
            "max": [
                200.0,
                50.0,
                10.0
            ],
            "darkness": 0.0
        }
    ]
})
