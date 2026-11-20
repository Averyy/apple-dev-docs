# Fill.ImageFill.Technique

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The technique the reader uses to fit the image to the fill area.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Fill.ImageFill.Technique
```

## Discussion

The technique also determines whether the image keeps its aspect ratio: one technique distorts the image to the area, two preserve the ratio (cropping the overhang or leaving the area showing through), and two show the image at a size of its own.

This value takes one of the following forms:

- `natural_size`: Draws the image once at its own size, scaled by `Fill.ImageFill.scale_percent`, centered in the area and clipped by it, so a larger image is cropped on all four sides and a smaller one leaves the area showing around it.
- `scale_to_fill`: Draws the image so that it keeps its aspect ratio and completely covers the filled area, cropping what overhangs on the longer axis.
- `scale_to_fit`: Draws the image so that it keeps its aspect ratio and fits completely within the filled area, which shows through on the two sides where the image falls short.
- `stretch`: Draws the image stretched over the filled area, scaling its width and height independently and distorting it unless the area already shares the image’s proportions.
- `tile`: Repeats the image at its own size, scaled by `Fill.ImageFill.scale_percent`, to cover the area. The first tile is placed at the filled area’s top-left corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.imagefill.technique)*