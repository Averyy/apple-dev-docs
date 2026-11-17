# input

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The scenario’s utterances joined into one line for the report’s input column.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var input: String { get }
```

## Discussion

Each utterance is quoted and joined with “→”. The report shows this value on one line, so it also lists each utterance in its turn’s `User Utterance` row.

## See Also

### Inspecting a scenario
- [let turns: [UserTurn]](./turns.md)
  The turns of the conversation in the order that the person says them.
- [var expected: SiriScenarioSubject.ScenarioReport?](./expected.md)
  The scenario’s expectations as the report’s Expected column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenario/input)*