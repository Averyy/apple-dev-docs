# sourceFrame

**Framework**: Video Toolbox  
**Kind**: property

The current source frame.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var sourceFrame: VTFrameProcessorFrame { get }
```

#### Discussion

This value must be non-nil.

## See Also

- [var nextFrame: VTFrameProcessorFrame?](vtframerateconversionparameters/nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtframerateconversionparameters/opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](vtframerateconversionparameters/interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/sourceframe)*