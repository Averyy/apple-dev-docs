# SiriTurnExpectationBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the expectations you attach to a user turn.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum SiriTurnExpectationBuilder
```

## Overview

Each `buildExpression` is a kind this level accepts; a kind without one here does not compile in this level’s block.

## Topics

### Building turn expectations
- [static func buildArray([SiriTurnExpectationBuilder.Component]) -> SiriTurnExpectationBuilder.Component](./siriturnexpectationbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock(SiriTurnExpectationBuilder.Component...) -> SiriTurnExpectationBuilder.Component](./siriturnexpectationbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: SiriTurnExpectationBuilder.Component) -> SiriTurnExpectationBuilder.Component](./siriturnexpectationbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: SiriTurnExpectationBuilder.Component) -> SiriTurnExpectationBuilder.Component](./siriturnexpectationbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static buildExpression(_:)](./siriturnexpectationbuilder/buildexpression%28_%29.md)
  Creates a component from a calls expectation.
- [static func buildOptional(SiriTurnExpectationBuilder.Component?) -> SiriTurnExpectationBuilder.Component](./siriturnexpectationbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.
### Defining components
- [SiriTurnExpectationBuilder.Component](./siriturnexpectationbuilder/component.md)
  What an expectation block builds.

## See Also

### Creating a user turn with expectations
- [init(String, () -> SiriTurnExpectationBuilder.Component)](./userturn/init%28_,_%29.md)
  Creates a turn from an utterance and what Siri should do in response to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriturnexpectationbuilder)*