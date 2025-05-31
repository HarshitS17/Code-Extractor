import pytesseract
import os
from PIL import Image

def extract_code_from_frames(frame_folder="frames"):
    code_output = []

    for filename in sorted(os.listdir(frame_folder)):
        if filename.endswith(".jpg"):
            image_path = os.path.join(frame_folder, filename)
            img = Image.open(image_path)

            text = pytesseract.image_to_string(img)

            if "{" in text or ";" in text or "#" in text or "()" in text:
                code_output.append(f"--- {filename} ---\n{text.strip()}\n")

    final_code = "\n".join(code_output)

    # Save to file
    os.makedirs("output", exist_ok=True)
    with open("output/code_output.txt", "w", encoding="utf-8") as f:
        f.write(final_code)

    return final_code

if __name__ == "__main__":
    code = extract_code_from_frames()
    print(code if code else "No code found in frames.")
