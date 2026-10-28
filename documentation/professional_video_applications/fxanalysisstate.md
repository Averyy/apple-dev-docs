# FxAnalysisState

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

The possible states of frame analysis, as reported by the host application.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
typealias FxAnalysisState = Int
```

```c
typedef NSUInteger FxAnalysisState;
```

## Discussion

Query the analysis state with [`analysisStateForEffect()`](./fxanalysisapi/analysisstateforeffect%28%29.md).

## Parameters

- `kFxAnalysisState_NotAnalyzing`: Not currently analyzing.
- `kFxAnalysisState_AnalysisRequested`: Analysis requested.
- `kFxAnalysisState_AnalysisStarted`: Analysis started.
- `kFxAnalysisState_AnalysisCompleted`: Analysis completed.
- `kFxAnalysisState_AnalysisInterrupted`: Analysis interrupted.

## Topics

### States of Analysis
- [var kFxAnalysisState_NotAnalyzing: FxAnalysisState](./kfxanalysisstate_notanalyzing.md)
  Not currently analyzing.
- [var kFxAnalysisState_AnalysisRequested: FxAnalysisState](./kfxanalysisstate_analysisrequested.md)
  Analysis requested.
- [var kFxAnalysisState_AnalysisStarted: FxAnalysisState](./kfxanalysisstate_analysisstarted.md)
  Analysis started.
- [var kFxAnalysisState_AnalysisCompleted: FxAnalysisState](./kfxanalysisstate_analysiscompleted.md)
  Analysis completed.
- [var kFxAnalysisState_AnalysisInterrupted: FxAnalysisState](./kfxanalysisstate_analysisinterrupted.md)
  Analysis interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalysisstate)*