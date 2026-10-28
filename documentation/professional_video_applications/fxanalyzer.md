# FxAnalyzer

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
protocol FxAnalyzer
```

```objc
@protocol FxAnalyzer
```

## Mentions

- [Analyzing media](../Professional-Video-Applications/analyzing-media.md)

## Overview

Implement this protocol if your plug-in needs to analyze some or all of the frames your plug-in is applied to before being able to render.

## Topics

### Analyzing Frames in Your Plug-in
- [func desiredAnalysisTimeRange(UnsafeMutablePointer<CMTimeRange>!, forInputWith: CMTimeRange) throws](./fxanalyzer/desiredanalysistimerange%28_,forinputwith%29.md)
  Requests the specified time range of frames you want to analyze.
- [func setupAnalysis(for: CMTimeRange, frameDuration: CMTime) throws](./fxanalyzer/setupanalysis%28for,frameduration%29.md)
  Completes any setup work before starting the frame analysis.
- [func analyzeFrame(FxImageTile!, at: CMTime) throws](./fxanalyzer/analyzeframe%28_,at%29.md)
  Analyzes the next frame.
- [func cleanupAnalysis() throws](./fxanalyzer/cleanupanalysis%28%29.md)
  Completes any necessary cleanup work after your plug-in’s frame analysis.
### Determining the Analysis State
- [typealias FxAnalysisState](./fxanalysisstate.md)
  The possible states of frame analysis, as reported by the host application.

## See Also

### Time and analysis
- [Understanding time in FxPlug](../Professional-Video-Applications/understanding-time-in-fxplug.md)
  Learn about time handling in host apps and plug-ins.
- [Scheduling media in plug-ins](../Professional-Video-Applications/scheduling-media-in-plug-ins.md)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
- [protocol FxTimingAPI_v4](./fxtimingapi_v4.md)
  A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.
- [protocol FxKeyframeAPI_v3](./fxkeyframeapi_v3.md)
  A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.
- [Analyzing media](../Professional-Video-Applications/analyzing-media.md)
  Use the FxPlug analysis API to analyze frames of source media before rendering them.
- [protocol FxAnalysisAPI](./fxanalysisapi.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalysisAPI_v2](./fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalyzer)*