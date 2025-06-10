# init(frameWidth:frameHeight:numberOfInterpolatedFrames:)

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
init?(frameWidth: Int, frameHeight: Int, numberOfInterpolatedFrames: Int)
```

#### Discussion

The available interpolation points will be be the next value of  (2^x -1) which is greater than or equal to numberOfInterpolatedFrames.  For example, if 1 interpolated frame is requested, 1 interpolation point at 0.5 is available.  If 2 interpolated frames are requested, 3 interpolation points at 0.25, 0.5 and 0.75 are available.  Not all available interpolation points need to be used.  Setting a higher numberOfInterpolatedFrames increases the resolution of interpolation in some cases, but will also increase latency.

## Parameters

- `frameWidth`: Width of source frame in pixels.
- `frameHeight`: Height of source frame in pixels.
- `numberOfInterpolatedFrames`: The number of uniformly spaced frames that you want to have available for interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/init(framewidth:frameheight:numberofinterpolatedframes:))*