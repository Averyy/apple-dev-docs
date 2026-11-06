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
static func buildEither(second component: [any AppEntityExpectationProviding]) -> [any AppEntityExpectationProviding]
```

## See Also

### Building results
- [static func buildArray([[any AppEntityExpectationProviding]]) -> [any AppEntityExpectationProviding]](./buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([any AppEntityExpectationProviding]...) -> [any AppEntityExpectationProviding]](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [any AppEntityExpectationProviding]) -> [any AppEntityExpectationProviding]](./buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildExpression(some AppEntityExpectationProviding) -> [any AppEntityExpectationProviding]](./buildexpression%28_%29.md)
  Creates a component from an app entity.
- [static func buildOptional([any AppEntityExpectationProviding]?) -> [any AppEntityExpectationProviding]](./buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/entityfindexpectationbuilder/buildeither(second:))*