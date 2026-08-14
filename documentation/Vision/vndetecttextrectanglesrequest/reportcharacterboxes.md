# reportCharacterBoxes

**Framework**: Vision  
**Kind**: property

A Boolean value that indicates whether the request detects character bounding boxes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var reportCharacterBoxes: Bool { get set }
```

#### Discussion

Set the value to [`true`](https://developer.apple.com/documentation/swift/true) to have the detector return character bounding boxes as an array of [`VNRectangleObservation`](vnrectangleobservation.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttextrectanglesrequest/reportcharacterboxes)*