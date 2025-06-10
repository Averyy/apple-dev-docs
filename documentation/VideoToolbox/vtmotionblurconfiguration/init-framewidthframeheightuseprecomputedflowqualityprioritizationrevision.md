# init(frameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new motion blur configuration with specified flow width and height.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, usePrecomputedFlow: Bool, qualityPrioritization: VTMotionBlurConfiguration.QualityPrioritization, revision: VTMotionBlurConfiguration.Revision)
```

#### Discussion

Initialization fails if the dimensions are out of range or revision is unsupported.

## Parameters

- `frameWidth`: The width of the source frame in pixels. Maximum value is 8192 pixels for macOS, and 4096 pixels for iOS.
- `frameHeight`: The height of the source frame in pixels. Maximum value is 4320 pixels for macOS, and 2160 pixels for iOS.
- `usePrecomputedFlow`: If true it indicates that the optical flow will be provided by the user, if false this configuration will compute the optical flow on the fly.
- `qualityPrioritization`: Instance to control quality and performance levels. See VEMotionBlurConfigurationQualityPrioritization for more information.
- `revision`: The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurconfiguration/init(framewidth:frameheight:useprecomputedflow:qualityprioritization:revision:))*