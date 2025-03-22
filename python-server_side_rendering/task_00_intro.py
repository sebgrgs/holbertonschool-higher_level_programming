#!/usr/bin/python3
"""
Creating a Simple Templating Program"
"""

def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees.
    """
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return

    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: All attendees must be dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        invitation = template

        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, "N/A")
            invitation = invitation.replace(f"{{{{ {key} }}}}", str(value))

        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as f:
            f.write(invitation)
