# VNHumanBodyPose3DObservation.HeightEstimation

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Constants that identify body height estimation techniques.

## Declaration

```swift
enum HeightEstimation
```

```c
enum VNHumanBodyPose3DObservationHeightEstimation : NSInteger;
```

## Topics

### Techniques
- [VNHumanBodyPose3DObservation.HeightEstimation.measured](./heightestimation-swift.enum/measured.md)
  A technique that uses LiDAR depth data to measure body height, in meters.
- [VNHumanBodyPose3DObservation.HeightEstimation.reference](./heightestimation-swift.enum/reference.md)
  A technique that uses a reference height.
- [VNHumanBodyPose3DObservation.HeightEstimation.measured](./heightestimation-swift.enum/measured.md)
  A technique that uses LiDAR depth data to measure body height, in meters.
- [VNHumanBodyPose3DObservation.HeightEstimation.reference](./heightestimation-swift.enum/reference.md)
  A technique that uses a reference height.
### Creating a Technique
- [init?(rawValue: Int)](./heightestimation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Body Height
- [var heightEstimation: VNHumanBodyPose3DObservation.HeightEstimation](./heightestimation-swift.property.md)
  The technique the framework uses to estimate body height.
- [var bodyHeight: Float](./bodyheight.md)
  The estimated human body height, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/heightestimation-swift.enum)*