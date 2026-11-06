# stream

**Framework**: Siri Evaluations  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence that delivers the scenarios in the order written.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var stream: any AsyncSequence<SiriScenario, any Error> { get }
```

## Discussion

It fails the run instead if the scenarios were to come from a file that couldn’t be read.

## See Also

### Loading scenarios
- [let scenarios: [SiriScenario]](./scenarios.md)
  The scenarios, in the order written.
- [SiriScenarioLoader.Sample](./sample.md)
  The type of sample this loader supplies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioloader/stream)*