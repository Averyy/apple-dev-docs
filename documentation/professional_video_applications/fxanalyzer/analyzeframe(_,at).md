# analyzeFrame(_:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Analyzes the next frame.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func analyzeFrame(_ frame: FxImageTile!, at frameTime: CMTime) throws
```

```objc
- (BOOL) analyzeFrame:(FxImageTile *) frame atTime:(CMTime) frameTime error:(NSError * *) error;
```

## Mentions

- [Analyzing media](../../Professional-Video-Applications/analyzing-media.md)

## Parameters

- `frame`: The current frame to analyze.
- `frameTime`: The time of the `frame` parameter.

## See Also

### Analyzing Frames in Your Plug-in
- [func desiredAnalysisTimeRange(UnsafeMutablePointer<CMTimeRange>!, forInputWith: CMTimeRange) throws](./desiredanalysistimerange%28_,forinputwith%29.md)
  Requests the specified time range of frames you want to analyze.
- [func setupAnalysis(for: CMTimeRange, frameDuration: CMTime) throws](./setupanalysis%28for,frameduration%29.md)
  Completes any setup work before starting the frame analysis.
- [func cleanupAnalysis() throws](./cleanupanalysis%28%29.md)
  Completes any necessary cleanup work after your plug-in’s frame analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalyzer/analyzeframe(_:at:))*