# createPattern

**Framework**: WebKit JS  
**Kind**: instm

Creates a pattern object using the specified image as a template. The pattern can be specified as repeating horizontally, vertically, both horizontally and vertically (the default), or not at all.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
CanvasPattern? createPattern(
    CanvasImageSource image, 
    DOMString repetition
);
```

#### Discussion

When specifying a stroke style or fill style, you can pass in a pattern object instead of a color. Subsequent drawing operations are stroked or filled using the specified image as a pattern. An image object can be obtained by setting a JavaScript variable equal to an HTML `img` element.

## Parameters

- `image`: An image object.
- `repeat`: An optional string. If the string value is  , the pattern repeats horizontally only. If the string value is  , the pattern repeats vertically only. If the string value is  , the pattern does not repeat. If this parameter is omitted, the pattern repeats both horizontally and vertically.

## See Also

- [createLinearGradient](canvasrenderingcontext2d/1630205-createlineargradient.md)
  Creates a linear gradient object with a specified start point and a specified end point.
- [createRadialGradient](canvasrenderingcontext2d/1631480-createradialgradient.md)
  Creates a radial gradient object using the cone defined by the specified starting and ending circles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1628866-createpattern)*