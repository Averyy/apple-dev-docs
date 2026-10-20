# VNPointsClassification

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

The set of classifications that describe how to interpret the points the region provides.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@frozen
enum VNPointsClassification
```

```c
enum VNPointsClassification : NSInteger;
```

## Topics

### Enumeration Cases
- [VNPointsClassification.closedPath](./vnpointsclassification/closedpath.md)
- [VNPointsClassification.disconnected](./vnpointsclassification/disconnected.md)
- [VNPointsClassification.openPath](./vnpointsclassification/openpath.md)
### Creating a Classification
- [init?(rawValue: Int)](./vnpointsclassification/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Describing Region Points
- [var pointsClassification: VNPointsClassification](./vnfacelandmarkregion2d/pointsclassification.md)
  An enumeration that describes how to interpret the points the region provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpointsclassification)*