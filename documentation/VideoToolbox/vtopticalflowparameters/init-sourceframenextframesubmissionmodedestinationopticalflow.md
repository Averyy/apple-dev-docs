# init(sourceFrame:nextFrame:submissionMode:destinationOpticalFlow:)

**Framework**: Video Toolbox  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+

## Declaration

```swift
init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame, submissionMode: VTOpticalFlowParameters.SubmissionMode, destinationOpticalFlow: VTFrameProcessorOpticalFlow)
```

## Parameters

- `sourceFrame`: The current source frame. This must be a non-nil value.
- `nextFrame`: The next source frame in presentation time order. This value can be set to nil for the last frame.
- `submissionMode`: A value describing the processing request in a parameters submission object.
- `destinationOpticalFlow`: A user allocated mutable optical flow that will receive the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowparameters/init(sourceframe:nextframe:submissionmode:destinationopticalflow:))*