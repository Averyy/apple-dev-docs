# fillRect

**Framework**: Webkitjs  
**Kind**: instm

Fills a specified rectangle in the current fill color, gradient, or pattern.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
void fillRect(
    unrestricted float x, 
    unrestricted float y, 
    unrestricted float width, 
    unrestricted float height
);
```

#### Discussion

All parameter values are in the canvas’s current coordinate system, subject to the current transformation matrix (rotation, scale, and so on).

## Parameters

- `x`: The x-coordinate of the left edge of the rectangle, in pixels from the left edge of the canvas coordinate system.
- `y`: The y-coordinate of the top edge of the rectangle, in pixels from the top of the canvas coordinate system.
- `width`: The width of the rectangle, in pixels.
- `height`: The height of the rectangle, in pixels.

## See Also

- [clearRect](canvasrenderingcontext2d/1632646-clearrect.md)
  Clears the specified rectangle to transparent black—RGBa(0,0,0,0).
- [strokeRect](canvasrenderingcontext2d/1632379-strokerect.md)
  Draws a rectangle using the current stroke color, pattern, or gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1633676-fillrect)*