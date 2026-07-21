# init(stage:gpuFamily:)

**Framework**: USDKit  
**Kind**: init

Creates a Metal-less player for the given USD stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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