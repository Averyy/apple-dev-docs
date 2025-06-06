# VNRecognizedObjectObservation

**Framework**: Vision  
**Kind**: class

A detected object observation with an array of classification labels that classify the recognized object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class VNRecognizedObjectObservation
```

#### Overview

The confidence of the classifications sum up to `1.0.` Multiply the classification confidence with the confidence of this observation.

## Topics

### Classifying a Recognized Object
- [var labels: [VNClassificationObservation]](vnrecognizedobjectobservation/labels.md)
  An array of observations that classify the recognized object.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.

## Relationships

### Inherits From
- [VNDetectedObjectObservation](vndetectedobjectobservation.md)
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

- [Recognizing Objects in Live Capture](recognizing-objects-in-live-capture.md)
  Apply Vision algorithms to identify objects in real-time video.
- [Understanding a Dice Roll with Vision and Object Detection](../coreml/model_integration_samples/understanding_a_dice_roll_with_vision_and_object_detection.md)
  Detect dice position and values shown in a camera frame, and determine the end of a roll by leveraging a dice detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedobjectobservation)*