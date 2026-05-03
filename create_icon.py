from PIL import Image, ImageDraw, ImageFont

# 256x256 is a standard icon size
size = (256, 256)
image = Image.new("RGBA", size, (255, 255, 255, 0)) # transparent background
draw = ImageDraw.Draw(image)

# Draw a blue hashtag
# We will draw it manually using rectangles to ensure it looks thick and solid
color = "#2196F3" # Material Blue
line_width = 30
margin = 40

# Horizontal lines
draw.rectangle([margin, margin + 50, size[0] - margin, margin + 50 + line_width], fill=color)
draw.rectangle([margin, size[1] - margin - 50 - line_width, size[0] - margin, size[1] - margin - 50], fill=color)

# Vertical lines
draw.rectangle([margin + 50, margin, margin + 50 + line_width, size[1] - margin], fill=color)
draw.rectangle([size[0] - margin - 50 - line_width, margin, size[0] - margin - 50, size[1] - margin], fill=color)

# Save as ICO
image.save("app_icon.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
print("Icon created successfully.")
