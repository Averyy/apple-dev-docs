# init(frameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new super-resolution scaler processor configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
init?(frameWidth: Int, frameHeight: Int, scaleFactor: Int, inputType: VTSuperResolutionScalerConfiguration.InputType, usePrecomputedFlow: Bool, qualityPrioritization: VTSuperResolutionScalerConfiguration.QualityPrioritization, revision: VTSuperResolutionScalerConfiguration.Revision)
```

#### Discussion

This processor increases resolution of an image or video. Returns `nil` if dimensions are out of range or revision is unsupported.

## Parameters

- `frameWidth`: Width of source frame in pixels. With  ,   maximum width is 1920 on macOS and 1440 on iOS. With  ,   maximum width is 1920.
- `frameHeight`: Height of source frame in pixels. With  ,   maximum height is 1080. With  , maximum height is 1920 on   macOS and 1080 on iOS.
- `scaleFactor`: Indicates the scale factor between input and output.
- `inputType`: Indicates the type of input, either video or image.
- `usePrecomputedFlow`: Boolean value to indicate that you provide optical flow; if false, this configuration   computes the optical flow on the fly.
- `qualityPrioritization`: A level you use to prioritize quality or performance; for more information about   supported levels, see  .
- `revision`: The specific algorithm or configuration revision you use to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/init(framewidth:frameheight:scalefactor:inputtype:useprecomputedflow:qualityprioritization:revision:))*