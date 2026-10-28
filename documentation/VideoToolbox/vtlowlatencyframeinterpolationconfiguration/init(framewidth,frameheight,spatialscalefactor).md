# init(frameWidth:frameHeight:spatialScaleFactor:)

**Framework**: Video Toolbox  
**Kind**: init  
**Role**: Initializer

Creates a new low-latency frame interpolation configuration for spatial scaling and temporal scaling.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, spatialScaleFactor: Int)
```

```objc
- (instancetype) initWithFrameWidth:(NSInteger) frameWidth frameHeight:(NSInteger) frameHeight spatialScaleFactor:(NSInteger) spatialScaleFactor;
```

## Discussion

When you configure the processor for spatial scaling, the low-latency frame interpolation processor only supports 2x spatial upscaling and a single frame of temporal interpolation at a 0.5 interpolation phase.

## Parameters

- `frameWidth`: Width of source frame in pixels.
- `frameHeight`: Height of source frame in pixels.
- `spatialScaleFactor`: The requested spatial scale factor as an integer. Currently, the processor supports only 2x spatial scaling.

## See Also

### Creating a frame interpolation configuration
- [init?(frameWidth: Int, frameHeight: Int, numberOfInterpolatedFrames: Int)](./init%28framewidth,frameheight,numberofinterpolatedframes%29.md)
  Creates a new low-latency frame interpolation configuration for frame-rate conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:spatialscalefactor:))*