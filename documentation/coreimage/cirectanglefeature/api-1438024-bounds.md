# bounds

**Framework**: Core Image  
**Kind**: instp

A rectangle indicating the position and extent of the feature in image coordinates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get }
```

#### Discussion

This property identifies the rectangular region  containing the detected rectangle, not necessarily the shape of the rectangle. A detected feature is rectangular in space, but may appear in perspective in the image. Use the properties listed in [`CIRectangleFeature`](cirectanglefeature.md) to find the corners of the rectangle as it appears in perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)*