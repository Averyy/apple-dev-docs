# globalAlpha

**Framework**: WebKit JS  
**Kind**: instp

A floating-point number controlling the degree of opacity for all drawing operations.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute unrestricted float globalAlpha;
```

#### Discussion

Set the `globalAlpha` to any value between 0 and 1, inclusive, to set the degree of opacity for all subsequent drawing operations, with 0 being completely transparent and 1 being completely opaque. Any pixels drawn subsequently have their alpha channel value multiplied by the `globalAlpha` value.

## See Also

- [globalCompositeOperation](canvasrenderingcontext2d/1632770-globalcompositeoperation.md)
  A string representing the compositing method for drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1631404-globalalpha)*