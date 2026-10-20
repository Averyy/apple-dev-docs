# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

Source frame that you provided when creating the low-latency frame interpolation parameters object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

```objc
@property (nonatomic, readonly) VTFrameProcessorFrame * sourceFrame;
```

## See Also

### Inspecting the parameters
- [var previousFrame: VTFrameProcessorFrame](./previousframe.md)
  Previous frame that you provided when creating the low-latency frame interpolation parameters object.
- [var interpolationPhase: [Float]](./interpolationphase-886vi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationparameters/sourceframe)*