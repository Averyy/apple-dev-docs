# nextFrame

**Framework**: Video Toolbox  
**Kind**: property

The next source frame in presentation time order.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
var nextFrame: VTFrameProcessorFrame? { get }
```

#### Discussion

For the last frame this value will be nil.

## See Also

- [var sourceFrame: VTFrameProcessorFrame](vtframerateconversionparameters/sourceframe.md)
  The current source frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](vtframerateconversionparameters/opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](vtframerateconversionparameters/interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](vtframerateconversionparameters/submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/nextframe)*