# strokeRect

**Framework**: WebKit JS  
**Kind**: instm

Draws a rectangle using the current stroke color, pattern, or gradient.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
void strokeRect(
    unrestricted float x, 
    unrestricted float y, 
    unrestricted float width, 
    unrestricted float height
);
```

#### Discussion

All parameter values are in the canvas’s current coordinate system, subject to the current transformation matrix (rotation, scale, and so on).

## Parameters

- `x`: The left edge of the rectangle, in units right from the origin of the canvas coordinate system.
- `y`: The top of the rectangle, in units down from the origin of the canvas coordinate system.
- `width`: The width of the rectangle, in canvas coordinate units.
- `height`: The height of the rectangle, in canvas coordinate units.

## See Also

- [clearRect](canvasrenderingcontext2d/1632646-clearrect.md)
  Clears the specified rectangle to transparent black—RGBa(0,0,0,0).
- [fillRect](canvasrenderingcontext2d/1633676-fillrect.md)
  Fills a specified rectangle in the current fill color, gradient, or pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1632379-strokerect)*