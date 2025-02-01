# Wave Visualization with Manim

This project visualizes a mathematical wave function using [Manim](https://www.manim.community/), a powerful Python animation engine for mathematical visualizations.

## Description
The script generates a graph of the function:

$\ f(x) = \sin(x) + \cos(\frac{x}{2}) $

This function combines elements of sine and cosine waves, creating an interesting wave interaction.

## Installation
Ensure you have Manim installed before running the script. If you haven't installed it yet, you can do so with:

```sh
pip install manim
```

Additionally, ensure you have NumPy installed:

```sh
pip install numpy
```

## Usage
Run the script using the following command:

```sh
manim -pql wave_script.py wave
```


This will generate and display the animation.

## Animation Example
![wave](https://github.com/user-attachments/assets/ffc05aa5-563e-4dc2-943f-8886ea0537b1)
## Features
- Uses Manim's `Axes` to create a coordinate plane
- Plots a mathematical function with Manim's `plot` method
- Creates two additional wave functions and transforms between them
- Customizes colors for visualization

## Future Improvements
- Add animation to show wave superposition dynamically
- Enhance the visual styling with labels and grid lines


