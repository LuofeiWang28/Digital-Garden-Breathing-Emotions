# ============================================================
# Project: Digital Garden: Breathing Emotions
# Author: Luofei Wang (25239575)
# Subject: 52685 Working with Data and Code — Code Prototype Project
#
# Description:
#   This generative art prototype visualises emotions through a “breathing flower”
#   that expands and contracts in rhythm with a digital breathing cycle.
#   The project demonstrates an understanding of time-based animation, easing,
#   colour interpolation, and interactive control using Processing (Python Mode).
#
# Originality & References:
#   All structure and logic are original work by Luofei Wang (25239575).
#   Easing and animation techniques were inspired by Daniel Shiffman’s
#   “The Nature of Code” (Chapter 3: Oscillation).
#   Source: https://natureofcode.com/book/chapter-3-oscillation/
#
# Features:
#   - Flower size “breathes” automatically
#   - A / D adjust pulse (“bouncing”) speed
#   - Emotions and colour transitions (1–4 keys)
#   - Optional rotation toggle (R key)
# ============================================================

# ---- Global variables: store animation settings and emotion state ----
period = 6000          # one full breath cycle (milliseconds)
angle = 0              # rotation angle
rotate_on = True       # Rotation toggle controlled by 'R'
pulse_speed = 1.0      # controls the flower's inner "jumping" speed

# ---- Colour states for transitions between emotions ----
curr_flower = None
target_flower = None
curr_bg = None
target_bg = None
trans = 1.0            # color transition progress (0–1)
current_emotion = "Calm"  # Label of the current emotion shown on screen

# ---- setup(): runs once to set canvas, colour mode, and initial state ----
def setup():
    global curr_flower, target_flower, curr_bg, target_bg, t0
    size(640, 640)
    colorMode(HSB, 360, 100, 100, 100)
    textAlign(CENTER)
    textSize(18)
    t0 = millis()

    # Start with CALM emotion (blue)
    curr_flower = target_flower = color(200, 50, 100)
    curr_bg = target_bg = color(200, 20, 12)
    
# ---- draw(): main animation loop that updates and draws each frame ----
def draw():
    global trans, curr_flower, curr_bg, angle

     # --- Calculate breathing phase based on elapsed time ---
    t = millis() - t0
    phase = TWO_PI * ((t % period) / period)
    breath = (sin(phase) + 1) * 0.5
    eased = breath * breath * (3 - 2 * breath)  # smooth in/out

   # --- Add a fast micro pulse for a "heartbeat" effect ---
    pulse = (sin(t * 0.005 * pulse_speed) + 1) * 0.5

     # --- Gradually blend colours toward the target emotion ---
    if trans < 1.0:
        trans += 0.02
        curr_flower = lerpColor(curr_flower, target_flower, trans)
        curr_bg = lerpColor(curr_bg, target_bg, trans)

    # --- Draw background with a subtle vignette effect ---
    background(curr_bg)

    # Subtle vignette
    noStroke()
    fill(hue(curr_bg), saturation(curr_bg), 6, 35)
    rect(0, 0, width, height)

    # Rotation
    if rotate_on:
        angle += 0.003 + 0.01 * eased

    # --- Draw the flower ---
    pushMatrix()
    translate(width/2, height/2 - 20)
    rotate(angle)

    # Radius changes with breathing + pulse
    r = 90 + 70 * eased + 10 * pulse

    # Glow layer
    fill(hue(curr_flower), saturation(curr_flower), 100, 18)
    ellipse(0, 0, r * 2.2, r * 2.2)

    # Petals
    petals = 8
    noStroke()
    for i in range(petals):
        a = TWO_PI / petals * i
        x = cos(a) * r
        y = sin(a) * r
        fill(curr_flower, 85)
        ellipse(x, y, r, r)

    # Center
    fill((hue(curr_flower)+25)%360, min(100, saturation(curr_flower)+10), 100)
    ellipse(0, 0, r * 0.7, r * 0.7)
    popMatrix()

    # --- Emotion label ---
    fill(0, 0, 100)
    textSize(22)
    text("Emotion: " + current_emotion, width/2, height/2 + 160)
        
# ---- keyPressed(): handle keyboard input for interaction ----        
def keyPressed():
    global rotate_on, pulse_speed
    # A / D control pulse (bouncing) speed
    if key in ('a', 'A'):
        pulse_speed = max(0.2, pulse_speed - 0.2)           # slower pulse
    elif key in ('d', 'D'):
        pulse_speed = min(5.0, pulse_speed + 0.2)           # faster pulse

    # Number keys switch emotional themes
    elif key == '1':
        set_emotion("Calm",  color(200, 50, 100), color(200, 20, 12))   # blue
    elif key == '2':
        set_emotion("Happy", color(50, 80, 100),  color(50, 25, 12))    # yellow
    elif key == '3':
        set_emotion("Stress",color(10, 90, 100),  color(10, 35, 10))    # red
    elif key == '4':
        set_emotion("Sad",   color(280, 50, 100), color(280, 25, 10))   # purple
        
    # R toggles rotation on/off
    elif key in ('r', 'R'):
        rotate_on = not rotate_on

# ---- set_emotion(): update emotion label and start colour transition ----
def set_emotion(label, flower_col, bg_col):
    global current_emotion, target_flower, target_bg, trans
    current_emotion = label            # Update displayed emotion name
    target_flower = flower_col         # New flower colour to transition to
    target_bg = bg_col                 # New background colour
    trans = 0                          # Reset transition progress for smooth blending
