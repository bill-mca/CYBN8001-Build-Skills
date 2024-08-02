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

# Limitations and Criticisms
We really need to take a step back and examine the solution proposed. It is limited in many ways by the tech that it depends on. The idea of using machine learning in this context should be called into question. The coffee shop owner should be encouraged to take a more holistic view of their problem rather than jumping to the conclusion that ML is a good solution. 
- The code above is severley hampered by its presumptuous understanding of temporal patterns. The barrista responsible for a coffee is assumed to have been visible near the coffee machine precisely 20 seconds before the coffee was served. Likewise, coffee is assumed to spend more than 20 but less than 40 seconds in the serving area. If a cup sits for too long it will be double counted. If it doesn't sit in the serving area for 20 seconds there is a risk of it being missed by the counter. Tracking the coffees is a potential state-of-the-art solution to this but it still wouldn't be flawless and it would be a lot more complicated to deploy.
- The algorithm will make mistakes assigning the barrista if there are multiple staff near the coffee machine.
- The temporal limitations mean that customers might need to wait an extra 20 seconds for their coffee.
- The image classification model might recognise many types of coffee but it will not be able to achieve perfect precision. There is too great of a diversity of types of coffee to recognize by sight alone. Consider the challenge of distinguishing a decaf soy latte from a regular latte. Without adding extra symbols (perhaps stickers or texta marks), I can't imagine the model will be able to get this right.
- To ensure the efficacy of the classifier, the cafe will need to use distinctive looking cups for its various types of coffee. This might directly detract from the profitability of the cafe and will certainly impact its brand coherency and aesthetics.
- As written, the algorithm is sensitive to the camera being bumped. Any time the camera is bumped an expert will need to fix the process one way or another.
- Likewise, if the coffee shop changes its layout, decor or the types of cups that it uses, an expert will need to retrain the model.

# Improvement
This was an exercise in using machine learning to solve a problem, but the problem was only vaguely defined. The most sensible pathways to improving the solution depend on more specific problem definition.

## Use the Till
Is it really necessary to get data on coffees made? Given all the challenges listed above, and the implications for the quality of the dataset, would it not be better to use invoice data from the shop's till to track the number and type of coffees made? If we want to know which barristas are making most of the difficult/obscure coffees, we could make some temporal assumption to align the till data with the QR nametag dataset from the camera without taking an expensive and fragile machine learning approach.

## Human Logging
If we need to track coffees at the very moment they are made, with precision down to the second, why not place a touchscreen beside the coffee machine that allows the barista to quickly log the type of coffee they've made?

## More Sensors
Alternatively, if it is essential to eliminate human error or deceit from this process, we could attach a microphone to the coffee machine. I believe that sound data of the machine in opperation will better identify the type of coffee being made than images can.  
 
