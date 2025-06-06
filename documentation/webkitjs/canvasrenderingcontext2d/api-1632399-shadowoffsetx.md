# shadowOffsetX

**Framework**: Webkitjs  
**Kind**: instp

A floating-point number that controls the horizontal offset of shadows from the elements casting the shadows.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
attribute unrestricted float shadowOffsetX;
```

#### Discussion

Shadows are cast `shadowOffsetX` pixels to the right, regardless of the canvas rotation, scale, or transformation. If `shadowOffsetX` is negative, shadows are cast to the left.

Shadows are cast if `shadowOffsetX` is nonzero and the alpha value of `shadowColor` is nonzero.

## See Also

- [clearShadow](canvasrenderingcontext2d/1634057-clearshadow.md)
  Turns shadows off.
- [shadowBlur](canvasrenderingcontext2d/1632236-shadowblur.md)
  A floating-point number that controls the degree of Gaussian blur applied to shadows.
- [shadowColor](canvasrenderingcontext2d/1629275-shadowcolor.md)
  A string that contains the RGBa color value of shadows. 
- [shadowOffsetY](canvasrenderingcontext2d/1633455-shadowoffsety.md)
  A floating-point number that controls the vertical offset of shadows from the elements casting the shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1632399-shadowoffsetx)*