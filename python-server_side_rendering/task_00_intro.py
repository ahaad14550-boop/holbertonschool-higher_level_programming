#!/usr/bin/python3
"""Module for generating invitation files from a template."""
import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee data.
    """
    # Check template type
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check attendees type
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check empty template
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate an invitation for each attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template

        # Replace placeholders
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        # Create output filename
        filename = f"output_{index}.txt"

        # Write the output file
        try:
            with open(filename, "w") as file:
                file.write(output)
        except OSError as error:
            print(f"Error writing to {filename}: {error}")