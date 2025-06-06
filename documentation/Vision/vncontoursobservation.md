# VNContoursObservation

**Framework**: Vision  
**Kind**: class

An object that represents the detected contours in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNContoursObservation
```

## Topics

### Inspecting the Observation
- [var contourCount: Int](vncontoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](vncontoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [VNContour]](vncontoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
- [var topLevelContourCount: Int](vncontoursobservation/toplevelcontourcount.md)
  The total number of detected top-level contours.
- [func contour(at: Int) throws -> VNContour](vncontoursobservation/contour(at:)-9on0y.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func contour(at: IndexPath) throws -> VNContour](vncontoursobservation/contour(at:)-52odo.md)
  Retrieves the contour object at the specified index path.
- [class VNContour](vncontour.md)
  A class that represents a detected contour in an image.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [var results: [VNContoursObservation]?](vndetectcontoursrequest/results.md)
  The results of the request to detect contours.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncontoursobservation)*