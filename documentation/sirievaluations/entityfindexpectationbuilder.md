# EntityFindExpectationBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the entities a finds expectation requires.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum EntityFindExpectationBuilder
```

## Topics

### Building results
- [static func buildArray([[any AppEntityExpectationProviding]]) -> [any AppEntityExpectationProviding]](./entityfindexpectationbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([any AppEntityExpectationProviding]...) -> [any AppEntityExpectationProviding]](./entityfindexpectationbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [any AppEntityExpectationProviding]) -> [any AppEntityExpectationProviding]](./entityfindexpectationbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: [any AppEntityExpectationProviding]) -> [any AppEntityExpectationProviding]](./entityfindexpectationbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(some AppEntityExpectationProviding) -> [any AppEntityExpectationProviding]](./entityfindexpectationbuilder/buildexpression%28_%29.md)
  Creates a component from an app entity.
- [static func buildOptional([any AppEntityExpectationProviding]?) -> [any AppEntityExpectationProviding]](./entityfindexpectationbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.

## See Also

### Creating a find expectation
- [init(() -> [any AppEntityExpectationProviding])](./finds/init%28_%29.md)
  Creates an expectation that Siri surfaces each entity in the block by search or resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/entityfindexpectationbuilder)*