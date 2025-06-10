# FaceObservation.Landmarks2D

**Framework**: Vision  
**Kind**: struct

A collection of facial features that a request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Landmarks2D
```

#### Overview

This represents the set of all detectable 2D face landmarks and regions, exposed as properties. The coordinates of the face landmarks are normalized to the dimensions of the face observation’s `FaceObservation/boundingBox`, with the origin at the bounding box’s lower-left corner.

## Topics

### Getting the landmarks
- [var faceContour: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/facecontour.md)
- [var innerLips: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/innerlips.md)
- [var leftEye: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/lefteye.md)
- [var leftEyebrow: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/lefteyebrow.md)
- [var leftPupil: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/leftpupil.md)
- [var medianLine: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/medianline.md)
- [var nose: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/nose.md)
- [var noseCrest: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/nosecrest.md)
- [var outerLips: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/outerlips.md)
- [var rightEye: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/righteye.md)
- [var rightEyebrow: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/righteyebrow.md)
- [var rightPupil: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/rightpupil.md)
### Inspecting a landmark
- [let originatingRequestDescriptor: RequestDescriptor?](faceobservation/landmarks2d/originatingrequestdescriptor.md)
### Getting all landmarks
- [var allPoints: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/allpoints.md)
- [FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/region.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [var landmarks: FaceObservation.Landmarks2D?](faceobservation/landmarks.md)
  The facial features of the detected face.
- [let pitch: Measurement<UnitAngle>](faceobservation/pitch.md)
  The pitch angle of a face.
- [let roll: Measurement<UnitAngle>](faceobservation/roll.md)
  The roll angle of a face.
- [let yaw: Measurement<UnitAngle>](faceobservation/yaw.md)
  The yaw angle of a face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/landmarks2d)*