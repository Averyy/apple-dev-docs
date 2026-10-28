# FaceObservation.Landmarks2D

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A collection of facial features that a request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct Landmarks2D
```

## Overview

This represents the set of all detectable 2D face landmarks and regions, exposed as properties. The coordinates of the face landmarks are normalized to the dimensions of the face observation’s [`boundingBox`](../boundingboxproviding/boundingbox.md), with the origin at the bounding box’s lower-left corner.

## Topics

### Getting the landmarks
- [var faceContour: FaceObservation.Landmarks2D.Region](./landmarks2d/facecontour.md)
- [var innerLips: FaceObservation.Landmarks2D.Region](./landmarks2d/innerlips.md)
- [var leftEye: FaceObservation.Landmarks2D.Region](./landmarks2d/lefteye.md)
- [var leftEyebrow: FaceObservation.Landmarks2D.Region](./landmarks2d/lefteyebrow.md)
- [var leftPupil: FaceObservation.Landmarks2D.Region](./landmarks2d/leftpupil.md)
- [var medianLine: FaceObservation.Landmarks2D.Region](./landmarks2d/medianline.md)
- [var nose: FaceObservation.Landmarks2D.Region](./landmarks2d/nose.md)
- [var noseCrest: FaceObservation.Landmarks2D.Region](./landmarks2d/nosecrest.md)
- [var outerLips: FaceObservation.Landmarks2D.Region](./landmarks2d/outerlips.md)
- [var rightEye: FaceObservation.Landmarks2D.Region](./landmarks2d/righteye.md)
- [var rightEyebrow: FaceObservation.Landmarks2D.Region](./landmarks2d/righteyebrow.md)
- [var rightPupil: FaceObservation.Landmarks2D.Region](./landmarks2d/rightpupil.md)
### Inspecting a landmark
- [let originatingRequestDescriptor: RequestDescriptor?](./landmarks2d/originatingrequestdescriptor.md)
### Getting all landmarks
- [var allPoints: FaceObservation.Landmarks2D.Region](./landmarks2d/allpoints.md)
- [FaceObservation.Landmarks2D.Region](./landmarks2d/region.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an observation
- [enum RequestDescriptor](../requestdescriptor.md)
  A type that describes the request and revision combination.
- [var landmarks: FaceObservation.Landmarks2D?](./landmarks.md)
  The facial features of the detected face.
- [let pitch: Measurement<UnitAngle>](./pitch.md)
  The pitch angle of a face.
- [let roll: Measurement<UnitAngle>](./roll.md)
  The roll angle of a face.
- [let yaw: Measurement<UnitAngle>](./yaw.md)
  The yaw angle of a face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/landmarks2d)*