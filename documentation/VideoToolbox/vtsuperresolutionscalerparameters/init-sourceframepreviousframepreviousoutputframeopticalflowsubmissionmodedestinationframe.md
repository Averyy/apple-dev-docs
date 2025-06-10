# init(sourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:)

**Framework**: Video Toolbox  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
init?(sourceFrame: VTFrameProcessorFrame, previousFrame: VTFrameProcessorFrame?, previousOutputFrame: VTFrameProcessorFrame?, opticalFlow: VTFrameProcessorOpticalFlow?, submissionMode: VTSuperResolutionScalerParameters.SubmissionMode, destinationFrame: VTFrameProcessorFrame)
```

#### Discussion

Init will return nil if sourceFrame or destinationFrame is nil, sourceFrame and reference frames  are different pixelFormats.

## Parameters

- `sourceFrame`: Current source frame. Must be non nil.
- `previousFrame`: The Previous source frame in presentation time order. For the first frame this can be set to nil.
- `previousOutputFrame`: The Previous output frame in presentation time order. For the first frame this can be set to nil.
- `opticalFlow`: Optional VTFrameProcessorOpticalFlow object that contains forward and backward optical flow between sourceFrame and previousFrame frame. Only needed if optical flow is pre-computed.
- `submissionMode`: Set to VTSuperResolutionScalerParametersSubmissionModeSequential to indicate that current submission follow presentation time order without jump or skip when compared to previous submission. VTSuperResolutionScalerParametersSubmissionModeSequential will yield better performance. Set to VTSuperResolutionScalerParametersSubmissionModeRandom to indicate a skip or a jump in frame sequence.
- `destinationFrame`: User allocated pixel buffer that will receive the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerparameters/init(sourceframe:previousframe:previousoutputframe:opticalflow:submissionmode:destinationframe:))*