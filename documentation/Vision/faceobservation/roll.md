# roll

**Framework**: Vision  
**Kind**: property

The roll angle of a face.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let roll: Measurement<UnitAngle>
```

#### Discussion

This value indicates the rotational angle of the face around the z-axis.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [FaceObservation.Landmarks2D](faceobservation/landmarks2d.md)
  A collection of facial features that a request detects.
- [var landmarks: FaceObservation.Landmarks2D?](faceobservation/landmarks.md)
  The facial features of the detected face.
- [let pitch: Measurement<UnitAngle>](faceobservation/pitch.md)
  The pitch angle of a face.
- [let yaw: Measurement<UnitAngle>](faceobservation/yaw.md)
  The yaw angle of a face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/roll)*