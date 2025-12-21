# init(sourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:)

**Framework**: Video Toolbox  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame?, previousFrame: VTFrameProcessorFrame?, nextOpticalFlow: VTFrameProcessorOpticalFlow?, previousOpticalFlow: VTFrameProcessorOpticalFlow?, motionBlurStrength: Int, submissionMode: VTMotionBlurParameters.SubmissionMode, destinationFrame: VTFrameProcessorFrame)
```

## Parameters

- `sourceFrame`: The current source frame. This must be a non-nil value.
- `nextFrame`: The next source frame in presentation time order. This value can be set to nil for the last frame.
- `previousFrame`: The previous source frame in presentation time order. This value can be set to nil for the first frame.
- `nextOpticalFlow`: Optional optical flow object that contains forward and backward optical flow with the next frame. For the last frame this will always be nil. This object is only needed if optical flow is pre-computed.
- `previousOpticalFlow`: Optional optical flow object that contains forward and backward optical flow with the next frame. For the first frame this will always be nil. This object is only needed if optical flow is pre-computed.
- `motionBlurStrength`: Number to indicate the strength of blur to apply. This NSInteger number ranges from 1 to 100. The default value is 50.
- `submissionMode`: A value describing the processing request in a parameters submission object.
- `destinationFrame`: A user-allocated pixel buffer that will receive the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmotionblurparameters/init(sourceframe:nextframe:previousframe:nextopticalflow:previousopticalflow:motionblurstrength:submissionmode:destinationframe:))*