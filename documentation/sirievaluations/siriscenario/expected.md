# expected

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The scenario’s expectations as the report’s Expected column.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var expected: SiriScenarioSubject.ScenarioReport? { get }
```

## Discussion

One row per thing each expectation checks, keyed as the subject’s report keys it, so Xcode flags exactly the checks that failed. Built from the scenario alone, as EvalKit requires. `nil` when the scenario expects nothing.

## See Also

### Inspecting a scenario
- [let turns: [UserTurn]](./turns.md)
  The turns of the conversation in the order that the person says them.
- [var input: String](./input.md)
  The scenario’s utterances joined into one line for the report’s Input column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenario/expected)*