# analysisStateForEffect()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fetches the state of frame analysis for your plug-in.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func analysisStateForEffect() -> FxAnalysisState
```

```objc
- (FxAnalysisState) analysisStateForEffect;
```

## Mentions

- [Analyzing media](../../Professional-Video-Applications/analyzing-media.md)

#### Return Value

An analysis state ([`FxAnalysisState`](../fxanalysisstate.md)) of not analyzing, requested, started analyzing, completed, or interrupted.

## See Also

### Providing Frame Analysis Information
- [func startForwardAnalysis(FxAnalysisLocation) throws](./startforwardanalysis%28_%29.md)
  Requests that the application begin a forwards analysis of a clip from start to end.
- [func startBackwardAnalysis(FxAnalysisLocation) throws](./startbackwardanalysis%28_%29.md)
  Requests that the application begin a backwards analysis of a clip from end to start.
- [typealias FxAnalysisLocation](../fxanalysislocation.md)
  Indicates the type of hardware to use for analysis, either CPU or GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalysisapi/analysisstateforeffect())*