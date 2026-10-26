# FxAnalysisAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
protocol FxAnalysisAPI
```

```objc
@protocol FxAnalysisAPI
```

## Mentions

- [Analyzing media](https://developer.apple.com/documentation/professional-video-applications/analyzing-media)

#### Overview

Host applications implement this protocol to provide frame analysis information to plug-ins that support the FxAnalyzer protocol.

## Topics

### Providing Frame Analysis Information
- [func analysisStateForEffect() -> FxAnalysisState](./fxanalysisapi/analysisstateforeffect%28%29.md)
  Fetches the state of frame analysis for your plug-in.
- [func startForwardAnalysis(FxAnalysisLocation) throws](./fxanalysisapi/startforwardanalysis%28_%29.md)
  Requests that the application begin a forwards analysis of a clip from start to end.
- [func startBackwardAnalysis(FxAnalysisLocation) throws](./fxanalysisapi/startbackwardanalysis%28_%29.md)
  Requests that the application begin a backwards analysis of a clip from end to start.
- [typealias FxAnalysisLocation](./fxanalysislocation.md)
  Indicates the type of hardware to use for analysis, either CPU or GPU.

## Relationships

### Inherited By
- [FxAnalysisAPI_v2](./fxanalysisapi_v2.md)

## See Also

### Time and analysis
- [Understanding time in FxPlug](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug)
  Learn about time handling in host apps and plug-ins.
- [Scheduling media in plug-ins](https://developer.apple.com/documentation/professional-video-applications/scheduling-media-in-plug-ins)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
- [protocol FxTimingAPI_v4](./fxtimingapi_v4.md)
  A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.
- [protocol FxKeyframeAPI_v3](./fxkeyframeapi_v3.md)
  A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.
- [Analyzing media](https://developer.apple.com/documentation/professional-video-applications/analyzing-media)
  Use the FxPlug analysis API to analyze frames of source media before rendering them.
- [protocol FxAnalysisAPI_v2](./fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalyzer](./fxanalyzer.md)
  A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalysisapi)*