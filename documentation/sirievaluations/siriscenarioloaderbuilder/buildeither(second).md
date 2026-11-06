# buildEither(second:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a component from the second branch of a conditional statement.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func buildEither(second component: SiriScenarioLoader) -> SiriScenarioLoader
```

## See Also

### Building loaders
- [static func buildArray([SiriScenarioLoader]) -> SiriScenarioLoader](./buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock(SiriScenarioLoader...) -> SiriScenarioLoader](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: SiriScenarioLoader) -> SiriScenarioLoader](./buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Creates a component from a scenario.
- [static func buildOptional(SiriScenarioLoader?) -> SiriScenarioLoader](./buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioloaderbuilder/buildeither(second:))*