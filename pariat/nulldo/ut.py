def get_data_with_extension(data, extension):
    # Check if the data is not None or empty
    if not data:
        raise ValueError("No data provided")

    # Check if the extension is valid
    if not isinstance(extension, str) or not extension.startswith('.'):
        raise ValueError("Invalid extension provided")

    # Return the data and extension as a tuple
    return data, extension

# Example usage:
# Assuming we have valid 'data' and 'extension' variables
# data = ...
# extension = ...
# result = get_data_with_extension(data, extension)
