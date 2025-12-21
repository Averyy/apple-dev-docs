# init(isContrastAndVibrancyEnhancementEnabled:pixelBufferProcessor:)

**Framework**: VisionKit  
**Kind**: init

Creates a view that renders a spatial camera region and optionally applies contrast enhancement.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(isContrastAndVibrancyEnhancementEnabled: Bool = false, pixelBufferProcessor: ((Result<CameraRegionView.PixelBufferProcessingContext, any Error>) async -> CVReadOnlyPixelBuffer?)? = nil)
```

## Parameters

- `isContrastAndVibrancyEnhancementEnabled`: Enabling this value improves the   overall visual richness and contrast of the frames.
- `pixelBufferProcessor`: Provides CVReadOnlyPixelBuffer for any additional   modifications that may need to be applied to the pixel buffer before   rendering the pixel buffer on the view. Any modification requires the   creation of a new CVReadOnlyPixelBuffer. Be mindful of the high   computational cost since it would impact the frame rate. Returning     will ignore the received frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/cameraregionview/init(iscontrastandvibrancyenhancementenabled:pixelbufferprocessor:))*