# SiriExpectationEvaluator

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An evaluator that grades a scenario against its expectations.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct SiriExpectationEvaluator
```

## Overview

It reports the metrics of each kind of expectation — [`Calls`](./calls.md), [`Finds`](./finds.md), [`OnScreen`](./onscreen.md), [`SiriResponse`](./siriresponse.md) and [`Loads`](./loads.md); a `Loads(.preferred)` is shown in the report but never graded. Return it from your evaluation’s `evaluators`, alone or with graders of your own, and call `computeSiriMetrics(into:)` from `aggregateMetrics(using:)` to show its metrics as the report’s summary cards.

## Topics

### Creating an evaluator
- [init()](./siriexpectationevaluator/init%28%29.md)
  Creates an evaluator that grades a scenario against its expectations.
### Grading a scenario
- [func metrics(subject: SiriScenarioSubject, input: SiriScenario) async throws -> [Metric]](./siriexpectationevaluator/metrics%28subject,input%29.md)
  Returns the metrics from grading the scenario’s expectations against its transcript.

## Relationships

### Conforms To
- [EvaluatorProtocol](../Evaluations/evaluatorprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Evaluations
- [enum SiriService](./siriservice.md)
  A service that runs a scenario through Siri and records what Siri does.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriexpectationevaluator)*