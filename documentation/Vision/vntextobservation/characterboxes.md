# characterBoxes

**Framework**: Vision  
**Kind**: property

An array of detected individual character bounding boxes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var characterBoxes: [VNRectangleObservation]? { get }
```

#### Discussion

If the associated [`VNDetectTextRectanglesRequest`](vndetecttextrectanglesrequest.md) request indicates interest in character boxes by setting the option `reportCharacterBoxes` to [`true`](https://developer.apple.com/documentation/Swift/true), this property is non-`nil`. If no characters are found, it remains empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntextobservation/characterboxes)*