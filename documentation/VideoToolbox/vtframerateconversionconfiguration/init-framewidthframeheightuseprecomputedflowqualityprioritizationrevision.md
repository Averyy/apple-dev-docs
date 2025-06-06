# init(frameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:)

**Framework**: Videotoolbox  
**Kind**: init

Creates a new frame rate conversion configuration with specified flow width and height.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, usePrecomputedFlow: Bool, qualityPrioritization: VTFrameRateConversionConfiguration.QualityPrioritization, revision: VTFrameRateConversionConfiguration.Revision)
```

#### Discussion

Initialization fails if the dimensions are out of range or if the revision is unsupported.

## Parameters

- `frameWidth`: The width of source frame in pixels. The maximum value is 8192 pixels for macOS, and 4096 pixels for iOS.
- `frameHeight`: The height of source frame in pixels. The maximum value is 4320 pixels for macOS, and 2160 pixels for iOS.
- `usePrecomputedFlow`: If true the optical flow will be provided by the user, else this configuration will compute the optical flow on the fly.
- `qualityPrioritization`: Instance to control quality and performance levels. See VEFrameRateConversionConfigurationQualityPrioritization for more information.
- `revision`: The specific algorithm or configuration revision that is used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/init(framewidth:frameheight:useprecomputedflow:qualityprioritization:revision:))*