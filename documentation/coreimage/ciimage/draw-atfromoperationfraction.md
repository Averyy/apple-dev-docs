# draw(at:from:operation:fraction:)

**Framework**: Core Image  
**Kind**: method

Draws all or part of the image at the specified point in the current coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
func draw(at point: NSPoint, from fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)
```

#### Discussion

The image content is drawn at its current resolution and is not scaled unless the CTM of the current coordinate system itself contains a scaling factor. The image is otherwise positioned and oriented using the current coordinate system.

## Parameters

- `point`: The location in the current coordinate system at which to draw the image.
- `fromRect`: The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system.
- `op`: The compositing operation to use when drawing the image. For details, see  .
- `delta`: The opacity of the image, specified as a value from   to  . Specifying a value of   draws the image as fully transparent while a value of   draws the image as fully opaque. Values greater than   are interpreted as  .

## See Also

- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](ciimage/draw(in:from:operation:fraction:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/draw(at:from:operation:fraction:))*