# opticalFlow

**Framework**: Videotoolbox  
**Kind**: property

A property that defines the optical flow for an object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var opticalFlow: VTFrameProcessorOpticalFlow? { get }
```

#### Discussion

An optional VTFrameProcessorReadOnlyOpticalFlow contains the forward and backward optical flow of the next frame. This value is only needed if the optical flow is pre-computed. For the first frame it will always be nil.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtframerateconversionparameters/sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](vtframerateconversionparameters/nextframe.md)
  The next source frame in presentation time order.
- [var interpolationPhase: [Float]](vtframerateconversionparameters/interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [var destinationFrames: [VTFrameProcessorFrame]](vtframerateconversionparameters/destinationframes.md)
  A caller-allocated array of frames that contains the pixel buffers to receive the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/opticalflow)*