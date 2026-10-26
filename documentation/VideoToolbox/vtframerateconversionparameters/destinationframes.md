# destinationFrames

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

A caller-allocated array of frames that contains the pixel buffers to receive the results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<VTFrameProcessorFrame *> * destinationFrames;
```

#### Discussion

This array must contain the same number of elements as the `interpolationPhase` property.

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  The current source frame.
- [var nextFrame: VTFrameProcessorFrame?](./nextframe.md)
  The next source frame in presentation time order.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./opticalflow.md)
  A property that defines the optical flow for an object.
- [interpolationPhase](./interpolationphase-6wdns.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/destinationframes)*