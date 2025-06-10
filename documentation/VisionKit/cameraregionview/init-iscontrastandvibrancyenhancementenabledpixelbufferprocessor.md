# init(isContrastAndVibrancyEnhancementEnabled:pixelBufferProcessor:)

**Framework**: VisionKit  
**Kind**: init

Creates a view that renders a spatial camera region, and optionally applies contrast enhancement.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(isContrastAndVibrancyEnhancementEnabled: Bool = false, pixelBufferProcessor: ((Result<CameraRegionView.PixelBufferProcessingContext, any Error>) async -> CVReadOnlyPixelBuffer?)? = nil)
```

## Parameters

- `isContrastAndVibrancyEnhancementEnabled`: Enabling this improves the overall visual richness and contrast of the frames.
- `pixelBufferProcessor`: Provides CVReadOnlyPixelBuffer for any additional modifications that may need   to be applied to the pixel buffer before rendering the pixel buffer on the view.   Note that any modification requires creation of a new CVReadOnlyPixelBuffer.   Be mindful of high computational cost as it would impact the frame rate.   Returning ‘nil’ will ignore the received frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/cameraregionview/init(iscontrastandvibrancyenhancementenabled:pixelbufferprocessor:))*