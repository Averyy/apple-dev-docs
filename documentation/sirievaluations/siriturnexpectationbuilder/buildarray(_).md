# buildArray(_:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a component by combining the components from each iteration of a loop.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func buildArray(_ components: [SiriTurnExpectationBuilder.Component]) -> SiriTurnExpectationBuilder.Component
```

## See Also

### Building turn expectations
- [static func buildBlock(SiriTurnExpectationBuilder.Component...) -> SiriTurnExpectationBuilder.Component](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: SiriTurnExpectationBuilder.Component) -> SiriTurnExpectationBuilder.Component](./buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: SiriTurnExpectationBuilder.Component) -> SiriTurnExpectationBuilder.Component](./buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Creates a component from a calls expectation.
- [static func buildOptional(SiriTurnExpectationBuilder.Component?) -> SiriTurnExpectationBuilder.Component](./buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriturnexpectationbuilder/buildarray(_:))*