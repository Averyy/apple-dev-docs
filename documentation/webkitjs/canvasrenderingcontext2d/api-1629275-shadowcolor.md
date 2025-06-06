# shadowColor

**Framework**: Webkitjs  
**Kind**: instp

A string that contains the RGBa color value of shadows. 

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
attribute DOMString shadowColor;
```

#### Discussion

The value may be any CSS color value. If the alpha value of `shadowColor` is nonzero, shadows are cast, provided that at least one of the three properties `shadowBlur`, `shadowOffsetX`, or `shadowOffsetY` is also nonzero.

## See Also

- [clearShadow](canvasrenderingcontext2d/1634057-clearshadow.md)
  Turns shadows off.
- [shadowBlur](canvasrenderingcontext2d/1632236-shadowblur.md)
  A floating-point number that controls the degree of Gaussian blur applied to shadows.
- [shadowOffsetX](canvasrenderingcontext2d/1632399-shadowoffsetx.md)
  A floating-point number that controls the horizontal offset of shadows from the elements casting the shadows.
- [shadowOffsetY](canvasrenderingcontext2d/1633455-shadowoffsety.md)
  A floating-point number that controls the vertical offset of shadows from the elements casting the shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1629275-shadowcolor)*