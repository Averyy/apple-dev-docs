# opticalFlow

**Framework**: Video Toolbox  
**Kind**: property

Optional object that contains forward and backward optical flow with the previous frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var opticalFlow: VTFrameProcessorOpticalFlow? { get }
```

#### Discussion

You only need this if optical flow is pre-computed. For the first frame this is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/opticalflow)*