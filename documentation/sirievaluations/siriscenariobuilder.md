# SiriScenarioBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the turns of a scenario.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum SiriScenarioBuilder
```

## Topics

### Building scenarios
- [static func buildArray([[UserTurn]]) -> [UserTurn]](./siriscenariobuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([UserTurn]...) -> [UserTurn]](./siriscenariobuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [UserTurn]) -> [UserTurn]](./siriscenariobuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: [UserTurn]) -> [UserTurn]](./siriscenariobuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(UserTurn) -> [UserTurn]](./siriscenariobuilder/buildexpression%28_%29.md)
  Creates a component from a user turn.
- [static func buildOptional([UserTurn]?) -> [UserTurn]](./siriscenariobuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.

## See Also

### Creating a scenario
- [init(() -> [UserTurn])](./siriscenario/init%28_%29.md)
  The turns of the conversation, in order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenariobuilder)*