# isPointInPath

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Determines whether a specified point is within the area defined by the current path.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
boolean isPointInPath(
    DOMPath path, 
    unrestricted float x, 
    unrestricted float y, 
    optional CanvasWindingRule winding
);
```

## Return Value

Returns `true` if the point is within the path.

## Discussion

All parameter values are in the canvas’s current coordinate system, subject to the current transformation matrix (rotation, scale, and so on).

## Parameters

- `x`: The x-coordinate of the point in the canvas coordinate system.
- `y`: The y-coordinate of the point in the canvas coordinate system.

## See Also

### Creating Paths (Lines, Curves, Arcs, and Shapes)
- [beginPath](./api-1632556-beginpath.md)
  Denotes the beginning of new path.
- [clip](./api-1631003-clip.md)
  Constrains the clipping region of the canvas to the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631233-ispointinpath)*