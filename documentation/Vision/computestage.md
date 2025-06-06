# ComputeStage

**Framework**: Vision  
**Kind**: enum

Types that represent the compute stage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum ComputeStage
```

#### Overview

The main compute stage represents the essential functionality of a request. Requests that provide additional analysis — or conversion of the data by the main stage — can also report a post-processing stage.

## Topics

### Getting the compute stages
- [ComputeStage.main](computestage/main.md)
  A stage that represents where the system performs the main functionality.
- [ComputeStage.postProcessing](computestage/postprocessing.md)
  A stage that represents where the system performs additional analysis after the main compute stage.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class VideoProcessor](videoprocessor.md)
  An object that performs offline analysis of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/computestage)*