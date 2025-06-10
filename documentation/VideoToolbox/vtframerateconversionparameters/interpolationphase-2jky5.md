# interpolationPhase

**Framework**: Video Toolbox  
**Kind**: property

An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
var interpolationPhase: [Float] { get }
```

#### Discussion

Array size indicates how many frames are needed to interpolate and needs to match destinationFrames array size, where there is one interval for each destination frame. Float number values should be between 0 and 1, e.g. to insert one frame in the middle, a value of 0.5 can be used.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtframerateconversionparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](vtframerateconversionparameters/nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtframerateconversionparameters/opticalflow.md)
  A property that defines the optical flow for an object.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/interpolationphase-2jky5)*