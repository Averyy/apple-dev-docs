# init(sourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a new frame rate conversion parameters object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
convenience init?(sourceFrame: VTFrameProcessorFrame, nextFrame: VTFrameProcessorFrame, opticalFlow: VTFrameProcessorOpticalFlow?, interpolationPhase: [Float], submissionMode: VTFrameRateConversionParameters.SubmissionMode, destinationFrames: [VTFrameProcessorFrame])
```

#### Discussion

Initialization fails if the `sourceFrame` or `nextFrame` arguments are `NULL`, if `sourceFrame` and reference frames don’t have the same pixel format, or if the `interpolationPhase` array count does not match the `destinationFrames` array count.

## Parameters

- `sourceFrame`: The current source frame. This must be a non nil value.
- `nextFrame`: The next source frame in presentation time order. This value can be set to nil for the last frame.
- `opticalFlow`: A property that defines the optical flow for an object. An optional VTFrameProcessorReadOnlyOpticalFlow contains the forward and backward optical flow of the next frame. This value is only needed if the optical flow is pre-computed. For the first frame it will always be nil.
- `interpolationPhase`: Array of float numbers to indicate which intervals to insert a frame between the current and next frame. Array size indicates how many frames are needed to interpolate and needs to match destinationFrames size, where there is one interval for each destination frame. Float number values should be between 0 and 1, e.g. to insert one frame in the middle, a value of 0.5 can be used.
- `submissionMode`: A value describing the processing request in a parameters submission object.
- `destinationFrames`: A caller-allocated NSArray of VTFrameProcessorFrame that contains pixel buffers that receive the results. The array must contain the same number of elements as interpolationPhase NSArray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionparameters/init(sourceframe:nextframe:opticalflow:interpolationphase:submissionmode:destinationframes:))*