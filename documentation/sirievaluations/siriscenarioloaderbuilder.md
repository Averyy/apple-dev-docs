# SiriScenarioLoaderBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects scenarios into one dataset.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum SiriScenarioLoaderBuilder
```

## Topics

### Building loaders
- [static func buildArray([SiriScenarioLoader]) -> SiriScenarioLoader](./siriscenarioloaderbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock(SiriScenarioLoader...) -> SiriScenarioLoader](./siriscenarioloaderbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: SiriScenarioLoader) -> SiriScenarioLoader](./siriscenarioloaderbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: SiriScenarioLoader) -> SiriScenarioLoader](./siriscenarioloaderbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static buildExpression(_:)](./siriscenarioloaderbuilder/buildexpression%28_%29.md)
  Creates a component from a scenario.
- [static func buildOptional(SiriScenarioLoader?) -> SiriScenarioLoader](./siriscenarioloaderbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.

## See Also

### Creating a loader
- [init(() -> SiriScenarioLoader)](./siriscenarioloader/init%28_%29.md)
  Creates a loader that supplies the scenarios a builder closure produces, in the order written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioloaderbuilder)*