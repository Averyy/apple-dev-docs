# ContoursObservation

**Framework**: Vision  
**Kind**: struct

An object that represents the detected contours in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ContoursObservation
```

## Topics

### Creating an observation
- [init(VNContoursObservation)](contoursobservation/init(_:).md)
  Creates a contours observation.
### Inspecting an observation
- [var contourCount: Int](contoursobservation/contourcount.md)
  The total number of detected contours.
- [var normalizedPath: CGPath](contoursobservation/normalizedpath.md)
  The detected contours as a path object in normalized coordinates.
- [var topLevelContours: [ContoursObservation.Contour]](contoursobservation/toplevelcontours.md)
  An array of contours that don’t have another contour enclosing them.
### Getting the contours
- [ContoursObservation.Contour](contoursobservation/contour.md)
  An object that represents a detected contour in an image.
- [func contourAtIndex(Int) -> ContoursObservation.Contour?](contoursobservation/contouratindex(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](contoursobservation/countouratindexpath(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation)*