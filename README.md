# Digital Garden: Breathing Emotions

## 1. Overview
**Digital Garden: Breathing Emotions** is an interactive generative art prototype that visualizes human emotions through the rhythm of a “breathing” digital flower.  
Each flower expands and contracts in a calm, cyclical motion while its colors shift to express emotional states such as *Calm*, *Happy*, *Stress*, and *Sad*.  

The project explores how programming can be used as a medium for emotional expression and aesthetic experience.  
It demonstrates understanding of **time-based animation, easing functions, color interpolation, and interactivity** using **Processing (Python mode)**.  
Developed as part of the *52685 Working with Data and Code* subject at the **University of Technology Sydney**.

---

## Demo Image
[Digital Garden: Breathing Emotions1](demo1.png)
[Digital Garden: Breathing Emotions2](demo2.png)

*Figure 1. The “breathing flower” visualizes emotional states through rhythmic expansion and color transitions.*

---

## 2. How to Run
1. Open **Processing** and switch to **Python Mode**.  
2. Download this repository or clone it using Git.  
3. Open `Digital_Emotion_Garden.pyde` (or `sketch.pyde`) in Processing.  
4. Click **Run ▶** to start the animation.

### Controls
| Key | Function |
|-----|-----------|
| **A / D** | Slow down / Speed up the flower’s inner pulse |
| **1 – 4** | Switch between emotional themes *(Calm, Happy, Stress, Sad)* |
| **R** | Toggle rotation on/off |

---

## 3. Code Overview
- **setup()** — Initializes the canvas, color mode, and starting emotion.  
- **draw()** — Handles time-based animation, easing, and color interpolation.  
- **keyPressed()** — Enables interactive control of emotion, speed, and rotation.  
- **set_emotion()** — Switches between color palettes and initiates smooth transitions.  
- **Global Variables** — Manage breathing cycle (`period`), pulse speed, color states, and rotation.  

The code demonstrates key programming concepts:
- Variables and constants for state management  
- Functions for modular structure and reusability  
- Loops for drawing repeating petals  
- Trigonometric functions for generative motion  
- User input handling for interactivity  

---

## 4. Originality and References
All code structure and logic were written by **Luofei Wang (25239575)**.  
The easing method and conceptual inspiration were adapted from **Daniel Shiffman’s _The Nature of Code_ (Chapter 3: Oscillation)**.  
- Source: https://natureofcode.com/book/chapter-3-oscillation/  
- Accessed: 5 Oct 2025  

Processing Python Mode Reference: https://py.processing.org/reference/

---
