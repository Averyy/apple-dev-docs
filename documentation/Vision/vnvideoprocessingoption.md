# VNVideoProcessingOption

**Framework**: Vision  
**Kind**: struct

Options to pass to the video processor when adding requests.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct VNVideoProcessingOption
```

## Topics

### Options
- [static let frameCadence: VNVideoProcessingOption](vnvideoprocessingoption/framecadence.md)
  A value that indicates the video frame cadence at which to perform the video processing.
- [static let timeInterval: VNVideoProcessingOption](vnvideoprocessingoption/timeinterval.md)
  A value that indicates that the video processor should perform a request every -seconds.
### Initializers
- [init(rawValue: String)](vnvideoprocessingoption/init(rawvalue:).md)
  Creates an option with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessingoption)*