import comtypes.client
import json

certs_path = "C:\\Users\\Devyash\\Desktop\\pptEditor\\useful\\certs"

with open("standings.json", "r") as file:
    users = json.load(file)

def convert_pptx_to_pdf(powerpoint, input_file, output_file):
    try:
        presentation = powerpoint.Presentations.Open(input_file, WithWindow=False)
        
        presentation.SaveAs(output_file, FileFormat=32)  
        presentation.Close()
        powerpoint.Quit()
        
        print(f"✅ Conversion successful: {output_file}")
    except Exception as e:
        print(f"❌ Failed to convert {input_file} to PDF: {str(e)}")
        
for user in users:
    sub = "winners" if user["standing"] <= 10 else "loosers"
    
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1
    convert_pptx_to_pdf(powerpoint, f"{certs_path}\\{sub}\\{user["team_id"]}_{user["name"]}.pptx", f"{certs_path}\\{sub}\\pdfs\\{user["team_id"]}_{user["name"]}.pdf")