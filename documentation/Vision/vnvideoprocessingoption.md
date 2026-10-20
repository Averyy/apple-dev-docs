# VNVideoProcessingOption

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

Options to pass to the video processor when adding requests.

**Availability**:
- iOS 14.0+ - Deprecated in 14.0 (renamed: VNVideoProcessor.RequestProcessingOptions)
- iPadOS 14.0+ - Deprecated in 14.0 (renamed: VNVideoProcessor.RequestProcessingOptions)
- Mac Catalyst 14.0+ - Deprecated in 14.0 (renamed: VNVideoProcessor.RequestProcessingOptions)
- macOS 11.0+ - Deprecated in 11.0 (renamed: VNVideoProcessor.RequestProcessingOptions)
- tvOS 14.0+ - Deprecated in 14.0 (renamed: VNVideoProcessor.RequestProcessingOptions)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: VNVideoProcessor.RequestProcessingOptions)

## Declaration

```swift
struct VNVideoProcessingOption
```

```c
typedef NSString * VNVideoProcessingOption;
```

## Topics

### Options
- [static let frameCadence: VNVideoProcessingOption](./vnvideoprocessingoption/framecadence.md)
  A value that indicates the video frame cadence at which to perform the video processing.
- [static let timeInterval: VNVideoProcessingOption](./vnvideoprocessingoption/timeinterval.md)
  A value that indicates that the video processor should perform a request every *n*-seconds.
### Initializers
- [init(rawValue: String)](./vnvideoprocessingoption/init%28rawvalue%29.md)
  Creates an option with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Utilities
- [struct VNComputeStage](./vncomputestage.md)
  Types that represent the compute stage.
- [class VNGeometryUtils](./vngeometryutils.md)
  Utility methods to determine the geometries of various Vision types.
- [class VNVideoProcessor](./vnvideoprocessor.md)
  An object that performs offline analysis of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessingoption)*