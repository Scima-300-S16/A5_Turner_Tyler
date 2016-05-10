add_library('sound')
# t turner 2016
# tturner@cca.edu

# the data file
add_library('minim')
minim = Minim(this)
dataFile = "Vietnam.csv"
# empty lists to hold the data (we'll use parallel lists for this example)
Ethnicity = []
Deaths = []

def setup():
    global diameter
    global sound
    sound = minim.loadFile("Marvin Gaye - What's Going On.mp3", 1024)
    sound.loop()
    size(1200, 700)
    background(255)
    diameter = min(width, height) * 0.75
    strokeWeight(1)
    noLoop()    # Run once and stop -- no need for animation here
    # set the color mode to hue/saturation/brightness so we can set hue values based on the data
    colorMode(HSB, 255)
    # load in the data from file
    loadData()
    printArray(PFont.list())
    f = createFont("GothamRnd-Light.otf", 24)
    textFont(f)

def loadData():
    # with the data file open for reading ('r') and with nickname f...
    with open(dataFile, 'r') as f:
        # keep track of what line we're on
        lineNum = 0
        # for every line in the dataFile (lines come in as strings)
        for line in f:
            # if we are not on the first line (where the headings are)
            if lineNum > 0:
                # split the string at the comma and assign the first part to category, 
                # and the second part to amount
                category, amount = line.split(',')
                # convert amount to a number and add it to the list
                Deaths.append(float(amount))
                # keep the category as a string and add it to the list
                Ethnicity .append(category)
            # count up
            lineNum += 1

def draw():
    background(255)
    fill(0)
    textSize(30)
    text('Vietnam War Casualities',50,50,50)
    textSize(10)
    text('Source:http://www.archives.gov/research/military/vietnam-war/casualty-statistics.html',50,70,50)
    fill(0)
    textSize(11)
    text('226',1050,405,500)
    text('139',1050,425,500)
    text('7,243',1050,445,500)
    text('349',1050,465,500)
    text('229',1050,485,500)
    text('49,830',1050,505,500)
   
    
    # move to the center of the window
    translate(500,400)
    # keep track of angle
    lastAngle = 0
    # iterate over the Deaths from the data file
    for amount in Deaths:
        # calculate the angle by mapping from the total amount range to 360 degrees
        angle = map(amount, 0, sum(Deaths), 0, 360)
        # set the hue of this color of this slice based on the amount value (saturation and brightness are both maxed out at 255)
        fill(map(amount, min(Deaths), max(Deaths), 20, 255),255,255)
        # draw an angle starting from the last slice (use the PIE mode to add strokes on all the edges)
        arc(0, 0, diameter, diameter, lastAngle, lastAngle + radians(angle), PIE)
        # keep track of where we left off, so we can start there next time
        lastAngle += radians(angle)
        
    # now we'll draw the key, move over to the right edge
    translate(400,0)
    # iterate over both the Deaths and the Ethnicity  using zip
    for amount, category in zip(Deaths, Ethnicity ):
        # choose the fill color the same way as we did last time
        fill(map(amount, min(Deaths), max(Deaths), 20, 255),255,255)
        # draw a rectangle
        ellipse(0, 0, 15, 15)
        # black text
        fill(0)
        textSize(11)
        # draw the category name inside the rectangle
        text(category, 30, 5)
        # move down a bit for the next one
        translate(0, 20)
        