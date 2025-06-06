# width

**Framework**: Webkitjs  
**Kind**: instp

An integer containing the width of the canvas in CSS pixels.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute unsigned long width;
```

#### Discussion

Setting the `width` or `height` property, even without changing it, clears the canvas to transparent black and resets all context settings to their defaults, including the coordinate system and transformation matrix. If the `width` attribute is not specified in the `<canvas>` tag, the default width is 300 pixels.

## See Also

- [height](htmlcanvaselement/1634228-height.md)
  An integer containing the height of the canvas in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlcanvaselement/1632871-width)*