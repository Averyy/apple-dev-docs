# OnScreenEntityExpectationBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the entities an onscreen expectation requires.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum OnScreenEntityExpectationBuilder
```

## Overview

Restricted to `ResolvableAppEntityExpectation`, unlike [`EntityFindExpectationBuilder`](./entityfindexpectationbuilder.md): a bare `AppEntityDefinition` (any instance of the type) or `EventEntity.expectIdentifier("…")` (a specific instance). A view is staged with entities the author already knows, so an onscreen expectation is identity-based; property-based `.expect(title: …)` does not compile here, by design.

## Topics

### Building results
- [static func buildArray([[any ResolvableAppEntityExpectation]]) -> [any ResolvableAppEntityExpectation]](./onscreenentityexpectationbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([any ResolvableAppEntityExpectation]...) -> [any ResolvableAppEntityExpectation]](./onscreenentityexpectationbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [any ResolvableAppEntityExpectation]) -> [any ResolvableAppEntityExpectation]](./onscreenentityexpectationbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: [any ResolvableAppEntityExpectation]) -> [any ResolvableAppEntityExpectation]](./onscreenentityexpectationbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(some ResolvableAppEntityExpectation) -> [any ResolvableAppEntityExpectation]](./onscreenentityexpectationbuilder/buildexpression%28_%29.md)
  Creates a component from an onscreen app entity.
- [static func buildOptional([any ResolvableAppEntityExpectation]?) -> [any ResolvableAppEntityExpectation]](./onscreenentityexpectationbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.

## See Also

### Creating an onscreen expectation
- [init(() -> [any ResolvableAppEntityExpectation])](./onscreen/init%28_%29.md)
  Creates an expectation that each entity in the block is onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/onscreenentityexpectationbuilder)*