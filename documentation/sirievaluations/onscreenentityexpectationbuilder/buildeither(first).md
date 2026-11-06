# buildEither(first:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Creates a component from the first branch of a conditional statement.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func buildEither(first component: [any ResolvableAppEntityExpectation]) -> [any ResolvableAppEntityExpectation]
```

## See Also

### Building results
- [static func buildArray([[any ResolvableAppEntityExpectation]]) -> [any ResolvableAppEntityExpectation]](./buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([any ResolvableAppEntityExpectation]...) -> [any ResolvableAppEntityExpectation]](./buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(second: [any ResolvableAppEntityExpectation]) -> [any ResolvableAppEntityExpectation]](./buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(some ResolvableAppEntityExpectation) -> [any ResolvableAppEntityExpectation]](./buildexpression%28_%29.md)
  Creates a component from an onscreen app entity.
- [static func buildOptional([any ResolvableAppEntityExpectation]?) -> [any ResolvableAppEntityExpectation]](./buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/onscreenentityexpectationbuilder/buildeither(first:))*