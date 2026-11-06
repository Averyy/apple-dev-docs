# init(_:expectation:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a scenario from its turns, plus expectations for the conversation as a whole.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(@SiriScenarioBuilder _ content: () -> [UserTurn], @SiriScenarioExpectationBuilder expectation: () -> SiriScenarioExpectationBuilder.Component)
```

## Discussion

The `expectation:` label and trailing-closure shape mirror EvalKit’s `Scenario`, so adopting it later is a rebuild.

## See Also

### Creating a scenario with expectations
- [enum SiriScenarioExpectationBuilder](../siriscenarioexpectationbuilder.md)
  A result builder that collects the expectations you attach to a scenario.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenario/init(_:expectation:))*