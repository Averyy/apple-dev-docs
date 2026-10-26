# desiredAnalysisTimeRange(_:forInputWith:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests the specified time range of frames you want to analyze.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func desiredAnalysisTimeRange(_ desiredRange: UnsafeMutablePointer<CMTimeRange>!, forInputWith inputTimeRange: CMTimeRange) throws
```

```objc
- (BOOL) desiredAnalysisTimeRange:(CMTimeRange *) desiredRange forInputWithTimeRange:(CMTimeRange) inputTimeRange error:(NSError * *) error;
```

## Mentions

- [Analyzing media](../../Professional-Video-Applications/analyzing-media.md)

## Parameters

- `desiredRange`: The specified time range.
- `inputTimeRange`: The input time range.

## See Also

### Analyzing Frames in Your Plug-in
- [func setupAnalysis(for: CMTimeRange, frameDuration: CMTime) throws](./setupanalysis%28for,frameduration%29.md)
  Completes any setup work before starting the frame analysis.
- [func analyzeFrame(FxImageTile!, at: CMTime) throws](./analyzeframe%28_,at%29.md)
  Analyzes the next frame.
- [func cleanupAnalysis() throws](./cleanupanalysis%28%29.md)
  Completes any necessary cleanup work after your plug-in’s frame analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalyzer/desiredanalysistimerange(_:forinputwith:))*