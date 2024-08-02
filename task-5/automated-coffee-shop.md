---
title: Automated Coffee Shop
---

# Assumptions

- According to the exercise, the only equipment available are an HD camera and name tags with barcodes. I won't use the till or a button pad. Nor can we directly sense when buttons are being pushed on the coffee machine.
- The client is an independent coffee shop. We're not trying to make an enormous scalable system for Starbucks. Starbucks would not deploy machine learning for this purpose, they would build custom coffee machines that sense and report user interaction.

# Overview

 - The solution I propose mostly uses simple computer vision code to process images of the coffee making area. QR coded nametags are algorithmically resolved into data identifying the barrista responsible for making coffees.
 - The coffees are then identified by an image classification model. I would adive using a pre-trained model such as ResNet as a starting point for fine-tuning a custom classifier that recognizes just the types of coffee made by the coffee shop. This will require me to replace the final classification layer of the pre-trained model with a new layer that matches the number of coffee types we want to classify.
 - Data to train the model will be obtained by manually labelling images of cups of coffee as served at the cafe. this dataset could be collected by setting up the HD camera in its intended location for several weeks before training the model.
 - It will be important to ensure that the data contains a good sample of all the different types and sizes of coffee that we intend to be able classify.
 - It will be important that the training images are a good representation of the range of environmental conditions expected in the shop. If the cafe's lighting is very different in winter compared to summer we might data from both seasons for example.
 - Accuracy will be a good metric for deciding whether the model is working well. In evaluating the model comparison of accuracy and precision should be made to ensure the model isn't overfitted.
 - The coffee shop will need to setup the cafe in a way that suits the ML model. This might include selecting distinctive looking coffee cups that help the model to distinguish different types of coffee. The approach assumes that the camera can be setup behind the coffee machine so that the barista's name tag is visible to the camera while they are working and that the "serving area" is also in shot and not obscured by the barista.
 - Staff will need to be trained to change their behaviour in a way that supports the function of the model. They will need to place every cup of coffee that they make into the "serving area" and leave it there for 20 seconds. see the criticisms section below.

# Architecture
an illustration/graph of the system architecture and workflow

# Algorithm
I have presented some pseudo-python code for the coffee tracking system below. This architecture uses only one machine learning model. The model is used to classify cups of coffee. Before running the image classifier, the raw photo from the camera is processed to crop out relevant parts of the image. The model takes one image every 20 seconds and passes it to the classifier.

## Code
```python
# Pixel coordinates of a box where freshly made coffees are
# placed before being served to the customer
serving_bbox = (12, 17, 29, 34)
# pixel coordinates of of a box that encloses the coffee machine
# and so anyone standing near it
machine_bbox = (601, 112, 1204, 456)

def preproccess_image(image):
    """Takes an image of the whole coffee counter and clips out two
    areas of interest that are used by other models. Namely, the coffee
    machine and the serving area."""

    return(crop(image, machine_bbox), crop(image, serving_bbox))

def identify_coffees(image):
    """Uses a machine-learning based image classifier to identify and
    list any cups of coffee and their sizes. The ML core of the model
    recognizes many seperate classes each corresponding to a type and
    size. For example there are seperate classes recognized for regular
    versus large espressos

    ----------

    Inputs:

      image (matrix)

      A raster image with RGB values for each pixel. The model expects an
      image tighly cropped to 1-4 cups of coffee. 

    ----------
    Outputs:

      coffees (list)

      returns a list of tuples indicating the types and sizes of coffee shown
      in the input image. For example:
        [("espresso", "single"), ("cappuccino", "regular")]

"""

def decode_qr_codes(image):
    """Returns a string corresponding to the data value of the largest QR
    code in the input image. If the image contains no QR codes it returns
    the string 'unknown' instead""" 

# Directly write our outputs into a CSV file
file = open("{}_coffee_log.csv".format(time.timestamp())

# The main loop of the script:
while True:
    active_frame = camera.capture()
    subframes = preproccess_image(active_frame)

    tn = time.timestamp()

    # For each of the coffees identified in the image of the serving area,
    # add a line to the output file with a timestamp, the name of the
    # barista and the type and size of coffee.
    for coffee in identify_coffees(subframes[2]):
        type, size = coffee
        output.append([tn, barrista, type, size].join(", ") + "\n")

    # Set the barista value after writing output to the file.
    # This reflects the assumption that the coffee that is being served
    # now was made by someone who was at the coffee machine during the
    # last time step. 
    barrista = decode_qr_code(subframes[1])
    # wait 20 seconds before looking for new coffees:
    time.sleep(20)
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
 
