# setupAnalysis(for:frameDuration:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Completes any setup work before starting the frame analysis.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func setupAnalysis(for analysisRange: CMTimeRange, frameDuration: CMTime) throws
```

```objc
- (BOOL) setupAnalysisForTimeRange:(CMTimeRange) analysisRange frameDuration:(CMTime) frameDuration error:(NSError * *) error;
```

## Mentions

- [Analyzing media](../../Professional-Video-Applications/analyzing-media.md)

## Parameters

- `analysisRange`: The analysis time range.
- `frameDuration`: The frame duration.

## See Also

### Analyzing Frames in Your Plug-in
- [func desiredAnalysisTimeRange(UnsafeMutablePointer<CMTimeRange>!, forInputWith: CMTimeRange) throws](./desiredanalysistimerange%28_,forinputwith%29.md)
  Requests the specified time range of frames you want to analyze.
- [func analyzeFrame(FxImageTile!, at: CMTime) throws](./analyzeframe%28_,at%29.md)
  Analyzes the next frame.
- [func cleanupAnalysis() throws](./cleanupanalysis%28%29.md)
  Completes any necessary cleanup work after your plug-in’s frame analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalyzer/setupanalysis(for:frameduration:))*