# VNRecognizedObjectObservation

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNRecognizedObjectObservation : VNDetectedObjectObservation
```

## Overview

The confidence of the classifications sum up to `1.0.` Multiply the classification confidence with the confidence of this observation.

## Topics

### Classifying a Recognized Object
- [var labels: [VNClassificationObservation]](./vnrecognizedobjectobservation/labels.md)
  An array of observations that classify the recognized object.
- [class VNClassificationObservation](./vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.

## Relationships

### Inherits From
- [VNDetectedObjectObservation](./vndetectedobjectobservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](./vnrequestrevisionproviding.md)

## See Also

### Object recognition
- [Recognizing Objects in Live Capture](./recognizing-objects-in-live-capture.md)
  Apply Vision algorithms to identify objects in real-time video.
- [Understanding a Dice Roll with Vision and Object Detection](../CoreML/understanding-a-dice-roll-with-vision-and-object-detection.md)
  Detect dice position and values shown in a camera frame, and determine the end of a roll by leveraging a dice detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedobjectobservation)*