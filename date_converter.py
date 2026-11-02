def converter_date_format(date_str, input_format, output_format):
    """
    Converts a date string from one format to another.

    Parameters:
    - date_str (str): The date string to convert.
    - input_format (str): The format of the input date string.
    - output_format (str): The desired format for the output date string.

    Returns:
    - str: The converted date string in the desired format.
    """
    from datetime import datetime

    # Parse the input date string into a datetime object
    date_obj = datetime.strptime(date_str, input_format)

    # Format the datetime object into the desired output format
    return date_obj.strftime(output_format)
