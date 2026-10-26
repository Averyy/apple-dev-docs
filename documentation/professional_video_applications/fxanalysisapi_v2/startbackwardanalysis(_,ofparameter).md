# startBackwardAnalysis(_:ofParameter:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests that the application begin a backward analysis of an image parameter from start to end.

**Availability**:
- FxPlug 4.2.2+

## Declaration

```swift
func startBackwardAnalysis(_ location: FxAnalysisLocation, ofParameter parameterID: UInt32) throws
```

```objc
- (BOOL) startBackwardAnalysis:(FxAnalysisLocation) location ofParameter:(UInt32) parameterID error:(NSError * *) error;
```

## Parameters

- `location`: `FxAnalysisLocation` type to choose to do analysis on either GPU or CPU.
- `parameterID`: The ID of the image parameter to analyze.

## See Also

### Analyzing Input from an Image Well
- [func startForwardAnalysis(FxAnalysisLocation, ofParameter: UInt32) throws](./startforwardanalysis%28_,ofparameter%29.md)
  Requests that the application begin a forward analysis of an image parameter from start to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalysisapi_v2/startbackwardanalysis(_:ofparameter:))*