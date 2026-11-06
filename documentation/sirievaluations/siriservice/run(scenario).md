# run(scenario:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Runs a scenario through Siri and returns what Siri did, for your evaluation to grade.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func run(scenario: SiriScenario) async throws -> SiriScenarioSubject
```

## Discussion

Call it from your evaluation’s `subject(from:)`, with any setup the scenario needs before it. If you clean up after it, record a failure instead of throwing: a `subject(from:)` that throws discards the run, so the scenario drops out of every average. It runs only in a UI test target.

If the run stops partway, the turns that ran are graded and the report’s Diagnostics shows how many completed. If it can’t start, it throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriservice/run(scenario:))*