# init(sourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new super-resolution scaler parameters instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
init?(sourceFrame: VTFrameProcessorFrame, previousFrame: VTFrameProcessorFrame?, previousOutputFrame: VTFrameProcessorFrame?, opticalFlow: VTFrameProcessorOpticalFlow?, submissionMode: VTSuperResolutionScalerParameters.SubmissionMode, destinationFrame: VTFrameProcessorFrame)
```

#### Discussion

Returns `nil` if `sourceFrame` or `destinationFrame` is `nil`, or if `sourceFrame` and reference frames have different pixel formats.

## Parameters

- `sourceFrame`: Current source frame; must be non  .
- `previousFrame`: The previous source frame in presentation time order. For the first frame you can set this to  .
- `previousOutputFrame`: The previous output frame in presentation time order. For the first frame you can set this to  .
- `opticalFlow`: Optional   object that contains forward and backward optical flow between the   and  . You only need this if optical flow is pre-computed.
- `submissionMode`: Provides a hint to let the processor know whether you are submitting frames in presentation   sequence. For more information about supported modes see  .
- `destinationFrame`: User-allocated pixel buffer that receives the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/init(sourceframe:previousframe:previousoutputframe:opticalflow:submissionmode:destinationframe:))*