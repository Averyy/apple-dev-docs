# init(sourceFrame:destinationFrame:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new low-latency, super-resolution scaler parameters object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(sourceFrame: VTFrameProcessorFrame, destinationFrame: VTFrameProcessorFrame)
```

## Parameters

- `sourceFrame`: Current source frame; must be non  .
- `destinationFrame`: User-allocated pixel buffer that receives the scaled processor output; must be non  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerparameters/init(sourceframe:destinationframe:))*