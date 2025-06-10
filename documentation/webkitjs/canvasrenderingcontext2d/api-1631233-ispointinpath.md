# isPointInPath

**Framework**: WebKit JS  
**Kind**: instm

Determines whether a specified point is within the area defined by the current path.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
boolean isPointInPath(
    DOMPath path, 
    unrestricted float x, 
    unrestricted float y, 
    optional CanvasWindingRule winding
);
```

#### Return_value

Returns `true` if the point is within the path.

#### Discussion

All parameter values are in the canvas’s current coordinate system, subject to the current transformation matrix (rotation, scale, and so on).

## Parameters

- `x`: The x-coordinate of the point in the canvas coordinate system.
- `y`: The y-coordinate of the point in the canvas coordinate system.

## See Also

- [beginPath](canvasrenderingcontext2d/1632556-beginpath.md)
  Denotes the beginning of new path.
- [clip](canvasrenderingcontext2d/1631003-clip.md)
  Constrains the clipping region of the canvas to the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631233-ispointinpath)*