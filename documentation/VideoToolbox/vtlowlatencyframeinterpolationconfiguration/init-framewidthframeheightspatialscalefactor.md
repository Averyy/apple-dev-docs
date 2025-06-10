# init(frameWidth:frameHeight:spatialScaleFactor:)

**Framework**: Video Toolbox  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, spatialScaleFactor: Int)
```

#### Discussion

When configured for spatial scaling, the VTLowLatencyFrameInterpolation processor only supports 2x spatial upscaling and a single frame of temporal interpolation at a 0.5 interpolation phase.  Setting the numberOfInterpolatedFrames property will be ignored in this case.

## Parameters

- `frameWidth`: Width of source frame in pixels.
- `frameHeight`: Height of source frame in pixels.
- `spatialScaleFactor`: The requested spatial scale factor as an integer.  Currently, only 2x spatial scaling is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:spatialscalefactor:))*