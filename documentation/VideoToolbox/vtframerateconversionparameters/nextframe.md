# nextFrame

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The next source frame in presentation time order.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var nextFrame: VTFrameProcessorFrame? { get }
```

```objc
@property (nonatomic, readonly, nullable) VTFrameProcessorFrame * nextFrame;
```

## Discussion

For the last frame this value will be nil.

## See Also

### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](./sourceframe.md)
  The current source frame.
- [var opticalFlow: VTFrameProcessorOpticalFlow?](./opticalflow.md)
  A property that defines the optical flow for an object.
- [var interpolationPhase: [Float]](./interpolationphase-2jky5.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [var submissionMode: VTFrameRateConversionParameters.SubmissionMode](./submissionmode-swift.property.md)
  A value describing the processing request in a parameters submission object.
- [VTFrameRateConversionParameters.SubmissionMode](./submissionmode-swift.enum.md)
  A value describing the processing request in a parameters submission object.
- [interpolationPhase](./interpolationphase-6wdns.md)
  An array of floating-point values that indicate which intervals to insert a frame between the current and next frame.
- [destinationFrames](./destinationframes.md)
  A caller-allocated array of frames that contains the pixel buffers to receive the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/nextframe)*