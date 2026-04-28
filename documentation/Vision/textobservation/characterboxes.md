# characterBoxes

**Framework**: Vision  
**Kind**: property

An array of detected individual character bounding boxes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let characterBoxes: [RectangleObservation]?
```

#### Discussion

If the associated [`DetectTextRectanglesRequest`](detecttextrectanglesrequest.md) indicates interest in character boxes by setting the option [`reportCharacterBoxes`](detecttextrectanglesrequest/reportcharacterboxes.md) to `true`, this property is non-`nil`. If no characters are found, it remains empty.

## See Also

- [struct RectangleObservation](rectangleobservation.md)
  An object that represents the four vertices of a detected rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/textobservation/characterboxes)*