# clearShadow

**Framework**: Webkitjs  
**Kind**: instm

Turns shadows off.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
void clearShadow();
```

#### Discussion

When you set a shadow color or shadow blur, and a shadow offset, all subsequent drawing operations include a shadow of the current color and blur, at the specified offset. The `clearShadow` method is a convenient way to turn shadows off.

> **Note**: The `clearShadow()` method is not currently part of the HTML5 specification. It is supported in Safari and other Webkit-based browsers.

## See Also

- [shadowBlur](canvasrenderingcontext2d/1632236-shadowblur.md)
  A floating-point number that controls the degree of Gaussian blur applied to shadows.
- [shadowColor](canvasrenderingcontext2d/1629275-shadowcolor.md)
  A string that contains the RGBa color value of shadows. 
- [shadowOffsetX](canvasrenderingcontext2d/1632399-shadowoffsetx.md)
  A floating-point number that controls the horizontal offset of shadows from the elements casting the shadows.
- [shadowOffsetY](canvasrenderingcontext2d/1633455-shadowoffsety.md)
  A floating-point number that controls the vertical offset of shadows from the elements casting the shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1634057-clearshadow)*