# shadowBlur

**Framework**: Webkitjs  
**Kind**: instp

A floating-point number that controls the degree of Gaussian blur applied to shadows.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
attribute unrestricted float shadowBlur;
```

#### Discussion

If shadows are enabled, each shadow has a Gaussian blur applied to its alpha value, with a standard deviation of `shadowBlur`. The `shadowBlur` value must be a positive number, and may be zero.

Shadows are cast if the value of the `shadowBlur` property is nonzero and the alpha value of `shadowColor` is nonzero.

## See Also

- [clearShadow](canvasrenderingcontext2d/1634057-clearshadow.md)
  Turns shadows off.
- [shadowColor](canvasrenderingcontext2d/1629275-shadowcolor.md)
  A string that contains the RGBa color value of shadows. 
- [shadowOffsetX](canvasrenderingcontext2d/1632399-shadowoffsetx.md)
  A floating-point number that controls the horizontal offset of shadows from the elements casting the shadows.
- [shadowOffsetY](canvasrenderingcontext2d/1633455-shadowoffsety.md)
  A floating-point number that controls the vertical offset of shadows from the elements casting the shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1632236-shadowblur)*