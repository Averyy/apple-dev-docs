# submissionMode

**Framework**: Videotoolbox  
**Kind**: property

A value describing the processing request in a parameters submission object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var submissionMode: VTFrameRateConversionParameters.SubmissionMode { get }
```

#### Discussion

Set to VTFrameRateConversionParametersSubmissionModeSequential to indicate that the current submission follows the presentation time order without jumping or skipping when compared to the previous submission. Using the submission mode sequential will yield better performance. Set to VTFrameRateConversionParametersSubmissionModeRandom to indicate a skip or a jump in frame sequence. If the submission mode random is set, the internal cache will be cleared during the processWithParameters call.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtframerateconversionparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](vtframerateconversionparameters/nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtframerateconversionparameters/opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](vtframerateconversionparameters/interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [var destinationFrames: [VTFrameProcessorFrame]](vtframerateconversionparameters/destinationframes.md)
  A caller-allocated array of frames that contains the pixel buffers to receive the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/submissionmode-swift.property)*