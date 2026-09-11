# init(stage:gpuFamily:)

**Framework**: USDKit  
**Kind**: init

Creates a Metal-less player for the given USD stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init(stage: USDStage, gpuFamily: MTLGPUFamily)
```

#### Discussion

`gpuFamily` is required for CPU-side texture processing.

## See Also

- [convenience init(stage: USDStage)](usdplayer/init(stage:).md)
  Creates a Metal-enabled player for the given USD stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/init(stage:gpufamily:))*