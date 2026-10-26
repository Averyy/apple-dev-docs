# cleanupAnalysis()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Completes any necessary cleanup work after your plug-in’s frame analysis.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func cleanupAnalysis() throws
```

```objc
- (BOOL) cleanupAnalysis:(NSError * *) error;
```

## Mentions

- [Analyzing media](https://developer.apple.com/documentation/professional-video-applications/analyzing-media)

## See Also

### Analyzing Frames in Your Plug-in
- [func desiredAnalysisTimeRange(UnsafeMutablePointer<CMTimeRange>!, forInputWith: CMTimeRange) throws](./desiredanalysistimerange%28_,forinputwith%29.md)
  Requests the specified time range of frames you want to analyze.
- [func setupAnalysis(for: CMTimeRange, frameDuration: CMTime) throws](./setupanalysis%28for,frameduration%29.md)
  Completes any setup work before starting the frame analysis.
- [func analyzeFrame(FxImageTile!, at: CMTime) throws](./analyzeframe%28_,at%29.md)
  Analyzes the next frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalyzer/cleanupanalysis())*