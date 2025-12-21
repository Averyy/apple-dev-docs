# init(frameWidth:frameHeight:numberOfInterpolatedFrames:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new low-latency frame interpolation configuration for frame-rate conversion.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, numberOfInterpolatedFrames: Int)
```

#### Discussion

The available interpolation points are the equal to the value of (2^x - 1), where x is equal to `numberOfInterpolatedFrames`. For example,

- If you request 1 interpolated frame, 1 interpolation point at 0.5 is available.
- If you request 2 interpolated frames, 3 interpolation points at 0.25, 0.5 and 0.75 are available. You don’t need to use all available interpolation points. Setting a higher `numberOfInterpolatedFrames` increases the resolution of interpolation in some cases, but also increases latency.

## Parameters

- `frameWidth`: Width of source frame in pixels.
- `frameHeight`: Height of source frame in pixels.
- `numberOfInterpolatedFrames`: The number of uniformly spaced frames that you want to be used for interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:numberofinterpolatedframes:))*