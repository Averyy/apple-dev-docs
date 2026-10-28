# landmarks

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The facial features of the detected face.

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
var landmarks: FaceObservation.Landmarks2D?
```

## Discussion

This value is `nil` for face observations produced by a [`DetectFaceRectanglesRequest`](../detectfacerectanglesrequest.md) analysis. Use the [`DetectFaceLandmarksRequest`](../detectfacelandmarksrequest.md) object to find facial features.

## See Also

### Inspecting an observation
- [enum RequestDescriptor](../requestdescriptor.md)
  A type that describes the request and revision combination.
- [FaceObservation.Landmarks2D](./landmarks2d.md)
  A collection of facial features that a request detects.
- [let pitch: Measurement<UnitAngle>](./pitch.md)
  The pitch angle of a face.
- [let roll: Measurement<UnitAngle>](./roll.md)
  The roll angle of a face.
- [let yaw: Measurement<UnitAngle>](./yaw.md)
  The yaw angle of a face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/landmarks)*