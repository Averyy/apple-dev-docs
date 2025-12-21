# contourCount

**Framework**: Vision  
**Kind**: property

The total number of detected contours.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var contourCount: Int { get }
```

#### Discussion

Use this value to determine the number of indices available for calling [`contourAtIndex(_:)`](contoursobservation/contouratindex(_:).md).

## See Also

- [var normalizedPath: CGPath](contoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [ContoursObservation.Contour]](contoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contourcount)*