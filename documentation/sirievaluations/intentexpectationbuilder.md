# IntentExpectationBuilder

**Framework**: Siri Evaluations  
**Kind**: enum  
**Role**: Enumeration

A result builder that collects the intents in a calls expectation.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@resultBuilder
enum IntentExpectationBuilder
```

## Overview

A bare `AppIntentDefinition` (match-any) and an `AppIntentExpectation` (`CreateEventIntent.expect(title:)`) are both `AppIntentExpectationProviding`, so one overload lowers either straight to an `any AppIntentExpectationProviding` — no separate definition/expectation paths.

## Topics

### Building results
- [static func buildArray([[any AppIntentExpectationProviding]]) -> [any AppIntentExpectationProviding]](./intentexpectationbuilder/buildarray%28_%29.md)
  Creates a component by combining the components from each iteration of a loop.
- [static func buildBlock([any AppIntentExpectationProviding]...) -> [any AppIntentExpectationProviding]](./intentexpectationbuilder/buildblock%28_%29.md)
  Creates a component by combining the components of a block.
- [static func buildEither(first: [any AppIntentExpectationProviding]) -> [any AppIntentExpectationProviding]](./intentexpectationbuilder/buildeither%28first%29.md)
  Creates a component from the first branch of a conditional statement.
- [static func buildEither(second: [any AppIntentExpectationProviding]) -> [any AppIntentExpectationProviding]](./intentexpectationbuilder/buildeither%28second%29.md)
  Creates a component from the second branch of a conditional statement.
- [static func buildExpression(some AppIntentExpectationProviding) -> [any AppIntentExpectationProviding]](./intentexpectationbuilder/buildexpression%28_%29.md)
  Creates a component from an app intent.
- [static func buildOptional([any AppIntentExpectationProviding]?) -> [any AppIntentExpectationProviding]](./intentexpectationbuilder/buildoptional%28_%29.md)
  Creates a component from a conditional statement with no alternative branch.

## See Also

### Creating a call expectation
- [init(Calls.Ordering, () -> [any AppIntentExpectationProviding])](./calls/init%28_,_%29.md)
  Creates an expectation that Siri calls the intents in the block, or doesn’t call them, as the ordering requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/intentexpectationbuilder)*