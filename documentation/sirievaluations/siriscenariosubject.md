# SiriScenarioSubject

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

A record of one scenario’s run through Siri, as the Evaluations framework sees it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct SiriScenarioSubject
```

## Topics

### Inspecting the subject
- [var value: SiriScenarioSubject.ScenarioReport](./siriscenariosubject/value.md)
  The run as the report shows it.
- [let siriTranscript: SiriTranscript](./siriscenariosubject/siritranscript.md)
  Every observation captured during the run.
### Reporting results
- [SiriScenarioSubject.ScenarioReport](./siriscenariosubject/scenarioreport.md)
  What the Xcode report shows for one scenario: Diagnostics, Scenario (if it has any expectations of its own), then each turn.

## Relationships

### Conforms To
- [EvaluationSubject](../Evaluations/evaluationsubject.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Results
- [struct SiriTranscript](./siritranscript.md)
  The immutable record of one scenario’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenariosubject)*