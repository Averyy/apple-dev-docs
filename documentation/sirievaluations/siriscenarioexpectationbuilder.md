# SiriScenarioExpectationBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the expectations you attach to a scenario.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum SiriScenarioExpectationBuilder
```

## Overview

Each `buildExpression` is a kind this level accepts; a kind without one here does not compile in this level’s block.

A scenario-level expectation is checked against every turn together, so this level takes `Calls`, `Finds`, `OnScreen` and `Loads`. `SiriResponse` is not one of them: a Siri response expectation is checked on the turn that produces the response, so it is written in a turn’s block only.

## Topics

### Building scenario expectations
- [static func buildArray([SiriScenarioExpectationBuilder.Component]) -> SiriScenarioExpectationBuilder.Component](./siriscenarioexpectationbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock(SiriScenarioExpectationBuilder.Component...) -> SiriScenarioExpectationBuilder.Component](./siriscenarioexpectationbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: SiriScenarioExpectationBuilder.Component) -> SiriScenarioExpectationBuilder.Component](./siriscenarioexpectationbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: SiriScenarioExpectationBuilder.Component) -> SiriScenarioExpectationBuilder.Component](./siriscenarioexpectationbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static buildExpression(_:)](./siriscenarioexpectationbuilder/buildexpression%28_%29.md)
  Creates a component from a calls expectation.
- [static func buildOptional(SiriScenarioExpectationBuilder.Component?) -> SiriScenarioExpectationBuilder.Component](./siriscenarioexpectationbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.
### Defining components
- [SiriScenarioExpectationBuilder.Component](./siriscenarioexpectationbuilder/component.md)
  What a scenario’s expectation block builds.

## See Also

### Creating a scenario with expectations
- [init(() -> [UserTurn], expectation: () -> SiriScenarioExpectationBuilder.Component)](./siriscenario/init%28_,expectation%29.md)
  Creates a scenario from its turns, plus expectations for the conversation as a whole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioexpectationbuilder)*