# VNPoint

**Framework**: Vision  
**Kind**: class

An immutable object that represents a single 2D point in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNPoint
```

## Topics

### Creating a Point
- [init(x: Double, y: Double)](vnpoint/init(x:y:).md)
  Creates a point object with the specified coordinates.
- [convenience init(location: CGPoint)](vnpoint/init(location:).md)
  Creates a point object from the specified Core Graphics point.
- [class func apply(VNVector, to: VNPoint) -> VNPoint](vnpoint/apply(_:to:).md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.
- [class var zero: VNPoint](vnpoint/zero.md)
  A point object that represents the origin.
### Inspecting a Point
- [var x: Double](vnpoint/x.md)
  The x-coordinate.
- [var y: Double](vnpoint/y.md)
  The y-coordinate.
- [var location: CGPoint](vnpoint/location.md)
  The Core Graphics point for this point.
### Calculating Distance
- [func distance(VNPoint) -> Double](vnpoint/distance(_:).md)
  Returns the distance to another point.
- [class func distance(VNPoint, VNPoint) -> Double](vnpoint/distance(_:_:).md)
  Calculates the distance between two points.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VNDetectedPoint](vndetectedpoint.md)
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

## See Also

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)
  Add the capability to detect human body poses to your app using the Vision framework.
- [Detecting Hand Poses with Vision](detecting-hand-poses-with-vision.md)
  Create a virtual drawing app by using Vision’s capability to detect hand poses.
- [class VNDetectHumanBodyPoseRequest](vndetecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [class VNDetectHumanHandPoseRequest](vndetecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [class VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
  An observation that provides the points the analysis recognized.
- [class VNHumanBodyPoseObservation](vnhumanbodyposeobservation.md)
  An observation that provides the body points the analysis recognized.
- [class VNHumanHandPoseObservation](vnhumanhandposeobservation.md)
  An observation that provides the hand points the analysis recognized.
- [class VNDetectedPoint](vndetectedpoint.md)
  An object that represents a normalized point in an image, along with a confidence value.
- [class VNRecognizedPoint](vnrecognizedpoint.md)
  An object that represents a normalized point in an image, along with an identifier label and a confidence value.
- [struct VNRecognizedPointKey](vnrecognizedpointkey.md)
  The data type for all recognized point keys.
- [struct VNRecognizedPointGroupKey](vnrecognizedpointgroupkey.md)
  The data type for all recognized-point group keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint)*