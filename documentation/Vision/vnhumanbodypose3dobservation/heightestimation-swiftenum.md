# VNHumanBodyPose3DObservation.HeightEstimation

**Framework**: Vision  
**Kind**: enum

Constants that identify body height estimation techniques.

## Declaration

```swift
enum HeightEstimation
```

## Topics

### Techniques
- [VNHumanBodyPose3DObservation.HeightEstimation.measured](vnhumanbodypose3dobservation/heightestimation-swift.enum/measured.md)
  A technique that uses LiDAR depth data to measure body height, in meters.
- [VNHumanBodyPose3DObservation.HeightEstimation.reference](vnhumanbodypose3dobservation/heightestimation-swift.enum/reference.md)
  A technique that uses a reference height.
- [VNHumanBodyPose3DObservation.HeightEstimation.measured](vnhumanbodypose3dobservation/heightestimation-swift.enum/measured.md)
  A technique that uses LiDAR depth data to measure body height, in meters.
- [VNHumanBodyPose3DObservation.HeightEstimation.reference](vnhumanbodypose3dobservation/heightestimation-swift.enum/reference.md)
  A technique that uses a reference height.
### Creating a Technique
- [init?(rawValue: Int)](vnhumanbodypose3dobservation/heightestimation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var heightEstimation: VNHumanBodyPose3DObservation.HeightEstimation](vnhumanbodypose3dobservation/heightestimation-swift.property.md)
  The technique the framework uses to estimate body height.
- [var bodyHeight: Float](vnhumanbodypose3dobservation/bodyheight.md)
  The estimated human body height, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/heightestimation-swift.enum)*