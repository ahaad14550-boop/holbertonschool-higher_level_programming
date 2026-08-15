def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Invalid template type: expected string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Invalid attendees type: expected a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        name = attendee.get("name")
        event_title = attendee.get("event_title")
        event_date = attendee.get("event_date")
        event_location = attendee.get("event_location")

        invitation = invitation.replace(
            "{name}", str(name) if name is not None else "N/A"
        )
        invitation = invitation.replace(
            "{event_title}",
            str(event_title) if event_title is not None else "N/A"
        )
        invitation = invitation.replace(
            "{event_date}",
            str(event_date) if event_date is not None else "N/A"
        )
        invitation = invitation.replace(
            "{event_location}",
            str(event_location) if event_location is not None else "N/A"
        )

        with open(f"output_{index}.txt", "w") as file:
            file.write(invitation)