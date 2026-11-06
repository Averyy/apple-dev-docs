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
static func buildEither(second component: [any AppIntentExpectationProviding]) -> [any AppIntentExpectationProviding]
```

## See Also

### Building results
- [static func buildArray([[any AppIntentExpectationProviding]]) -> [any AppIntentExpectationProviding]](./buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([any AppIntentExpectationProviding]...) -> [any AppIntentExpectationProviding]](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [any AppIntentExpectationProviding]) -> [any AppIntentExpectationProviding]](./buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildExpression(some AppIntentExpectationProviding) -> [any AppIntentExpectationProviding]](./buildexpression%28_%29.md)
  Creates a component from an app intent.
- [static func buildOptional([any AppIntentExpectationProviding]?) -> [any AppIntentExpectationProviding]](./buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/intentexpectationbuilder/buildeither(second:))*