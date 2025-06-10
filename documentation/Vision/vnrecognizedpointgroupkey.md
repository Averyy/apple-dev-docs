# VNRecognizedPointGroupKey

**Framework**: Vision  
**Kind**: struct

The data type for all recognized-point group keys.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct VNRecognizedPointGroupKey
```

## Topics

### Body Regions
- [static let bodyLandmarkRegionKeyFace: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/bodylandmarkregionkeyface.md)
  A group key identifying the face, which includes the eyes, ears, and nose.
- [static let bodyLandmarkRegionKeyTorso: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/bodylandmarkregionkeytorso.md)
  A group key identifying the torso, which includes the neck, shoulders, hips, and root.
- [static let bodyLandmarkRegionKeyRightArm: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/bodylandmarkregionkeyrightarm.md)
  A group key identifying the landmarks of the right arm.
- [static let bodyLandmarkRegionKeyLeftArm: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/bodylandmarkregionkeyleftarm.md)
  A group key identifying the landmarks of the left arm.
- [static let bodyLandmarkRegionKeyRightLeg: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/bodylandmarkregionkeyrightleg.md)
  A group key identifying the landmarks of the right leg.
- [static let bodyLandmarkRegionKeyLeftLeg: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/bodylandmarkregionkeyleftleg.md)
  A group key identifying the landmarks of the left leg.
### All Regions
- [static let all: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/all.md)
  A group key identifying all landmarks.
- [static let point3DGroupKeyAll: VNRecognizedPointGroupKey](vnrecognizedpointgroupkey/point3dgroupkeyall.md)
  A group key identifying all three-dimensional landmarks.
### Initializers
- [init(rawValue: String)](vnrecognizedpointgroupkey/init(rawvalue:).md)
  Creates a recognized point key with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class VNPoint](vnpoint.md)
  An immutable object that represents a single 2D point in an image.
- [class VNDetectedPoint](vndetectedpoint.md)
  An object that represents a normalized point in an image, along with a confidence value.
- [class VNRecognizedPoint](vnrecognizedpoint.md)
  An object that represents a normalized point in an image, along with an identifier label and a confidence value.
- [struct VNRecognizedPointKey](vnrecognizedpointkey.md)
  The data type for all recognized point keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointgroupkey)*