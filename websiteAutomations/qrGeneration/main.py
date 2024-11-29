import json
from pprint import pprint

import qrcode
from PIL import Image
import requests
import pprint

# Path to your logo image
logo_path = 'FlutterCopy_1.png'

standing = "First Place"
event_name = "TechHunt '24"

url = "https://hacktheplot.vercel.app/certificate/sign"

with open('standings.json', 'r') as file:
   standings_data = json.load(file)

pprint.pprint(standings_data)

for (index, entry) in enumerate(standings_data):
    team_id = entry["team_id"]
    name = entry["name"]
    data = {
        "name": entry['name'],
        "teamName": entry['team_name'],
        "standing": entry['standing'],
        "eventName": event_name
    }



    # # Request body
    # data = {
    #     "name": name,
    #     "teamName": team_name,
    #     "standing": standing,
    #     "eventName": event_name
    # }

    # Send POST request
    response = requests.post(url, json=data)
    response_json = response.json()
    extracted_url = response_json.get("url")

    # Print response
    print("Response Body:", response.text)

    # Path to save the final QR code image
    output_path = f"output/{team_id}_{name}.png"

    # Create the QR code
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,)
    qr.add_data(extracted_url)  # Add your data hereblob:https://colab.research.google.com/5fa2d968-8b4e-49cd-9228-277b05e0e3d8
    qr.make(fit=True)

    # Generate the QR code with transparent background
    qr_img = qr.make_image(
        fill_color="#c9c9c9",
        back_color="#171717",
        # image_factory=StyledPilImage,
        # module_drawer=CircleModuleDrawer()
    ).convert("RGBA")



    # Add the logo to the QR code
    logo = Image.open(logo_path).convert("RGBA")  # Ensure logo is in RGBA format

    # Resize logo to fit inside the QR code
    qr_size = qr_img.size[0]
    logo_size = qr_size // 4  # Adjust logo size relative to QR code size
    logo = logo.resize((logo_size, logo_size))

    # Calculate position for the logo
    logo_position = (
        (qr_size - logo_size) // 2,
        (qr_size - logo_size) // 2,
    )

    # Paste the logo onto the QR code (use logo as a mask for transparency)
    qr_img.paste(logo, logo_position, mask=logo)

    # Save the final QR code image with transparent background
    qr_img.save(output_path, "PNG")