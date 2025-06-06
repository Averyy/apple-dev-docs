# init(forwardFlow:backwardFlow:)

**Framework**: Videotoolbox  
**Kind**: init

Creates an object with forward and backward optical flow pixel buffers.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init?(forwardFlow: CVPixelBuffer, backwardFlow: CVPixelBuffer)
```

#### Discussion

Instances retain the buffers backing them. Returns NULL if a NULL CVPixelBuffer is provided or if CVPixelBuffers are not IOSurface backed.

## Parameters

- `forwardFlow`: A pixel buffer that contains forward optical flow. This value must be non-NULL and IOSurface backed.
- `backwardFlow`: A pixel buffer that contains backward optical flow. his value must be non-NULL and IOSurface backed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessoropticalflow/init(forwardflow:backwardflow:))*