# initWithSourceFrame:previousFrame:interpolationPhase:destinationFrames:

**Framework**: Video Toolbox  
**Kind**: method  
**Role**: Instance Method

Creates a new low-latency frame interpolation parameters object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (instancetype) initWithSourceFrame:(VTFrameProcessorFrame *) sourceFrame previousFrame:(VTFrameProcessorFrame *) previousFrame interpolationPhase:(NSArray<NSNumber *> *) interpolationPhase destinationFrames:(NSArray<VTFrameProcessorFrame *> *) destinationFrames;
```

## Parameters

- `sourceFrame`: Current frame to use for interpolation; must be non `nil`.
- `previousFrame`: Previous frame used for interpolation; must be non `nil`.
- `interpolationPhase`: Array of float numbers that indicate interpolation phase locations at which the processor interpolates the frames. Must be greater than 0 and less than 1.0; for example 0.5 is midway between the previous frame and the source frame. If you enable spatial scaling, the only supported interpolation phase is 0.5.
- `destinationFrames`: Caller-allocated array of `VTFrameProcessorFrame` to receive the interpolated frames. This must have the same number of elements as the the `interpolationPhase`. If you enable spatial scaling, it must also contain an element to hold the scaled version of sourceFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationparameters/initwithsourceframe:previousframe:interpolationphase:destinationframes:)*