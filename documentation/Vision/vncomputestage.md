# VNComputeStage

**Framework**: Vision  
**Kind**: struct

Types that represent the compute stage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct VNComputeStage
```

## Topics

### Get the Compute Stages
- [static let main: VNComputeStage](vncomputestage/main.md)
  A stage that represents where the system performs the main functionality.
- [static let postProcessing: VNComputeStage](vncomputestage/postprocessing.md)
  A stage that represents where the system performs additional analysis from the main compute stage.
### Create a Compute Stage
- [init(rawValue: String)](vncomputestage/init(rawvalue:).md)
  Creates a compute stage with the value you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class VNGeometryUtils](vngeometryutils.md)
  Utility methods to determine the geometries of various Vision types.
- [class VNVideoProcessor](vnvideoprocessor.md)
  An object that performs offline analysis of video content.
- [struct VNVideoProcessingOption](vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncomputestage)*