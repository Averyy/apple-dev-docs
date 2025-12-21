# topLevelContours

**Framework**: Vision  
**Kind**: property

An array of contours that don’t have another contour enclosing them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var topLevelContours: [ContoursObservation.Contour] { get }
```

#### Discussion

This array constitutes the top of the contour hierarchy. You can iterate over each Contour instance to determine its children.

## See Also

- [var contourCount: Int](contoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](contoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/toplevelcontours)*