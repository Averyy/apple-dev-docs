# buildExpression(_:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a component from a calls expectation.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func buildExpression(_ calls: Calls) -> SiriScenarioExpectationBuilder.Component
```

**Other overloads**:

```swift
static func buildExpression(_ finds: Finds) -> SiriScenarioExpectationBuilder.Component
```

```swift
static func buildExpression(_ loads: Loads) -> SiriScenarioExpectationBuilder.Component
```

```swift
static func buildExpression(_ onScreen: OnScreen) -> SiriScenarioExpectationBuilder.Component
```

## See Also

### Building scenario expectations
- [static func buildArray([SiriScenarioExpectationBuilder.Component]) -> SiriScenarioExpectationBuilder.Component](./buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock(SiriScenarioExpectationBuilder.Component...) -> SiriScenarioExpectationBuilder.Component](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: SiriScenarioExpectationBuilder.Component) -> SiriScenarioExpectationBuilder.Component](./buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: SiriScenarioExpectationBuilder.Component) -> SiriScenarioExpectationBuilder.Component](./buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildOptional(SiriScenarioExpectationBuilder.Component?) -> SiriScenarioExpectationBuilder.Component](./buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioexpectationbuilder/buildexpression(_:))*