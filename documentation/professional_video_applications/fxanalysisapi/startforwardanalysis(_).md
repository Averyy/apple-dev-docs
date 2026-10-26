# startForwardAnalysis(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests that the application begin a forwards analysis of a clip from start to end.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func startForwardAnalysis(_ location: FxAnalysisLocation) throws
```

```objc
- (BOOL) startForwardAnalysis:(FxAnalysisLocation) location error:(NSError * *) error;
```

## Parameters

- `location`: FxAnalysisLocation type to choose to do analysis on either GPU or CPU.

## See Also

### Providing Frame Analysis Information
- [func analysisStateForEffect() -> FxAnalysisState](./analysisstateforeffect%28%29.md)
  Fetches the state of frame analysis for your plug-in.
- [func startBackwardAnalysis(FxAnalysisLocation) throws](./startbackwardanalysis%28_%29.md)
  Requests that the application begin a backwards analysis of a clip from end to start.
- [typealias FxAnalysisLocation](../fxanalysislocation.md)
  Indicates the type of hardware to use for analysis, either CPU or GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalysisapi/startforwardanalysis(_:))*