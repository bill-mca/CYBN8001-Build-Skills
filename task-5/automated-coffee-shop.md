---
title: Automated Coffee Shop
---

# Assumptions

- According to the exercise the only equipment available are an HD camera and name tags with barcodes. I won't use the till or a button pad.
- 

# Architecture
an illustration/graph of the system architecture and workflow

# Process
I have writen some pseudo-python code for the coffee tracking system below. This architecture uses only one machine learning model. The model is used to classify cups of coffee

```python

# Pixel coordinates of a box where freshly made coffees are
# placed before being served to the customer
serving_bbox = (12, 17, 29, 34)
# pixel coordinates of of a box that encloses the coffee machine
# and so anyone standing in front of it
machine_bbox = (601, 112, 1204, 456)

def preproccess_image(image):
    return(crop(image, machine_bbox), crop(image, serving_bbox))

def new_coffees(image):

def identify_coffee(image):
"""

    Inputs:
        image (matrix)

        A raster image with RGB values for each pixel. The model expects an  
    -----
    Outputs:

        Coffee (list)

        returns a list of strings indicating the types of coffee shown in the
        input image. The 

def decode_qr_codes(image):

# Returns a list of any valid QR codes in the image

output = []
while True:
    active_frame = camera.capture()
    subframes = preproccess_image(active_frame)
    
    barrista = decode_qr_code(subframes[1])
    type, size = identify_coffee(subframes[2])
    output.append([time.now(), barrista, type, size].join(", ") + "\n")
file = open("{}_coffee_log.csv".format(time.date())
file.write(output)
file.close()
```

## Example Output Dataset

```csv
datetime, barrista, type, size
2024-07-28-06:22:18, Mark, espresso, single
2024-07-28-06:24:48, Greta, cappuccino, large
2024-07-28-06:25:31, Greta, decaf soy latte, large
```

# Overview

-train the model to recognise different sized coffee cups and types of coffee

## Criticisms
- You'll need really solid object tracking
- Will wig out if there are two people in front of the coffee machine
- There are two many types of coffee to recognise them from the outputs
- You're better off tracking detail from the invoices
- or maybe from sound instead of images

a brief description explaining how the models integrate into the system to achieve 
the outcome