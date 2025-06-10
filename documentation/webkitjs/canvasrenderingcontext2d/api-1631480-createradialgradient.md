# createRadialGradient

**Framework**: WebKit JS  
**Kind**: instm

Creates a radial gradient object using the cone defined by the specified starting and ending circles.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
CanvasGradient createRadialGradient(
    float x0, 
    float y0, 
    float r0, 
    float x1, 
    float y1, 
    float r1
);
```

#### Return_value

A radial gradient object.

#### Discussion

You must add at least a starting and ending color stop to a radial gradient before it can be used. The direction of the gradient is specified by the starting and ending circles. When setting the fill style or stroke style for drawing objects, you can pass in a radial gradient object instead of a color. Anything subsequently drawn or filled over the cone defined by the starting and ending circles of the gradient is rendered using the gradient as a color. Anything drawn outside the cone is rendered using the color stop of the nearest edge of the cone. All parameter values are in the canvas’s current coordinate system, subject to the current transformation matrix (rotation, scale, and so on).

## Parameters

- `x0`: The x-coordinate of the center of the starting circle, in pixels from the left edge of the canvas coordinate system.
- `y0`: The y-coordinate of the center of the starting circle, in pixels from the top of the canvas coordinate system.
- `r0`: The radius of the starting circle.
- `x1`: The x-coordinate of the center of the ending circle, in pixels from the left edge of the canvas coordinate system.
- `y1`: The y-coordinate of the center of the ending circle, in pixels from the top of the canvas coordinate system.
- `r1`: The radius of the ending circle.

## See Also

- [createLinearGradient](canvasrenderingcontext2d/1630205-createlineargradient.md)
  Creates a linear gradient object with a specified start point and a specified end point.
- [createPattern](canvasrenderingcontext2d/1628866-createpattern.md)
  Creates a pattern object using the specified image as a template. The pattern can be specified as repeating horizontally, vertically, both horizontally and vertically (the default), or not at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631480-createradialgradient)*