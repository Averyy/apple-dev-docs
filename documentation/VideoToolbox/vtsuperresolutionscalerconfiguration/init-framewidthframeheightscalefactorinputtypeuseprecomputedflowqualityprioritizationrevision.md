# init(frameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:)

**Framework**: Video Toolbox  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, scaleFactor: Int, inputType: VTSuperResolutionScalerConfiguration.InputType, usePrecomputedFlow: Bool, qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization, revision: VTSuperResolutionScalerConfiguration.Revision)
```

#### Discussion

Init will return nil if dimensions are out of range or revision is unsupported.

## Parameters

- `frameWidth`: Width of source frame in pixels. With VTSuperResolutionScalerConfigurationInputTypeVideo, maximum width is 1920 on macOS and 1440 on iOS. With VTSuperResolutionScalerConfigurationInputTypeImage, maximum width is 1920.
- `frameHeight`: Height of source frame in pixels. With VTSuperResolutionScalerConfigurationInputTypeVideo, maximum height is 1080. With VTSuperResolutionScalerConfigurationInputTypeImage, maximum height is 1920.
- `scaleFactor`: Indicates the scale factor between input and output.
- `inputType`: Indicates the type of input (video / image ).
- `usePrecomputedFlow`: Boolean value to indicate that Optical Flow will be provided by the user, if false this configuration will compute the optical flow on the fly.
- `qualityPrioritization`: Used to control quality and performance levels. See VTSuperResolutionScalerConfigurationQualityPrioritization for more info.
- `revision`: The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/init(framewidth:frameheight:scalefactor:inputtype:useprecomputedflow:qualityprioritization:revision:))*