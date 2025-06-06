# bodyHeight

**Framework**: Vision  
**Kind**: property

The estimated human body height, in meters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var bodyHeight: Float { get }
```

## Mentions

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)

#### Discussion

The framework returns an accurate height if [`heightEstimation`](vnhumanbodypose3dobservation/heightestimation-swift.property.md) is [`VNHumanBodyPose3DObservation.HeightEstimation.measured`](vnhumanbodypose3dobservation/heightestimation-swift.enum/measured.md); otherwise, it returns a [`VNHumanBodyPose3DObservation.HeightEstimation.reference`](vnhumanbodypose3dobservation/heightestimation-swift.enum/reference.md) height.

## See Also

- [var heightEstimation: VNHumanBodyPose3DObservation.HeightEstimation](vnhumanbodypose3dobservation/heightestimation-swift.property.md)
  The technique the framework uses to estimate body height.
- [VNHumanBodyPose3DObservation.HeightEstimation](vnhumanbodypose3dobservation/heightestimation-swift.enum.md)
  Constants that identify body height estimation techniques.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/bodyheight)*