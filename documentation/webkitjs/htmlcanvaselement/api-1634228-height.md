# height

**Framework**: WebKit JS  
**Kind**: instp

An integer containing the height of the canvas in CSS pixels.

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

```swift
attribute unsigned long height;
```

#### Discussion

Setting the `width` or `height` property, even without changing it, clears the canvas to transparent black and resets all context settings to their defaults, including the coordinate system and transformation matrix. If the `height` attribute is not specified in the `<canvas>` tag, the default height is 150 pixels.

## See Also

- [width](htmlcanvaselement/1632871-width.md)
  An integer containing the width of the canvas in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlcanvaselement/1634228-height)*