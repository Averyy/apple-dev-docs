# metrics(subject:input:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Instance Method

Returns the metrics from grading the scenario’s expectations against its transcript.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
nonisolated(nonsending)
func metrics(subject: SiriScenarioSubject, input: SiriScenario) async throws -> [Metric]
```

## Discussion

Throws if `subject` wasn’t run from `input`: pass `subject(from:)`’s own sample to `SiriService.run(scenario:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriexpectationevaluator/metrics(subject:input:))*