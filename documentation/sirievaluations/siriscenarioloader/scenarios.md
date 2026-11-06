# scenarios

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

The scenarios, in the order written.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
let scenarios: [SiriScenario]
```

## Discussion

This value is empty when they come from a file that the framework couldn’t read. Running the evaluation then fails with the reason.

## See Also

### Loading scenarios
- [var stream: any AsyncSequence<SiriScenario, any Error>](./stream.md)
  An asynchronous sequence that delivers the scenarios in the order written.
- [SiriScenarioLoader.Sample](./sample.md)
  The type of sample this loader supplies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioloader/scenarios)*