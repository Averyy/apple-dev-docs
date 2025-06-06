# VNRecognizedPointsObservation

**Framework**: Vision  
**Kind**: class

An observation that provides the points the analysis recognized.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNRecognizedPointsObservation
```

## Topics

### Inspecting the Observation
- [var availableKeys: [VNRecognizedPointKey]](vnrecognizedpointsobservation/availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](vnrecognizedpointsobservation/availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint](vnrecognizedpointsobservation/recognizedpoint(forkey:).md)
  Retrieves a recognized point for a key.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint]](vnrecognizedpointsobservation/recognizedpoints(forgroupkey:).md)
  Retrieves the recognized points for a key.
### Converting Points for Core ML
- [func keypointsMultiArray() throws -> MLMultiArray](vnrecognizedpointsobservation/keypointsmultiarray.md)
  Retrieves the grouping of normalized point coordinates and confidence scores in a format compatible with Core ML.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Inherited By
- [VNAnimalBodyPoseObservation](vnanimalbodyposeobservation.md)
- [VNHumanBodyPoseObservation](vnhumanbodyposeobservation.md)
- [VNHumanHandPoseObservation](vnhumanhandposeobservation.md)
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

- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)
  Add the capability to detect human body poses to your app using the Vision framework.
- [Detecting Hand Poses with Vision](detecting-hand-poses-with-vision.md)
  Create a virtual drawing app by using Vision’s capability to detect hand poses.
- [class VNDetectHumanBodyPoseRequest](vndetecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [class VNDetectHumanHandPoseRequest](vndetecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [class VNHumanBodyPoseObservation](vnhumanbodyposeobservation.md)
  An observation that provides the body points the analysis recognized.
- [class VNHumanHandPoseObservation](vnhumanhandposeobservation.md)
  An observation that provides the hand points the analysis recognized.
- [class VNPoint](vnpoint.md)
  An immutable object that represents a single 2D point in an image.
- [class VNDetectedPoint](vndetectedpoint.md)
  An object that represents a normalized point in an image, along with a confidence value.
- [class VNRecognizedPoint](vnrecognizedpoint.md)
  An object that represents a normalized point in an image, along with an identifier label and a confidence value.
- [struct VNRecognizedPointKey](vnrecognizedpointkey.md)
  The data type for all recognized point keys.
- [struct VNRecognizedPointGroupKey](vnrecognizedpointgroupkey.md)
  The data type for all recognized-point group keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation)*