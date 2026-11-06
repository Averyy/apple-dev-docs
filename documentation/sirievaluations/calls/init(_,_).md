# init(_:_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates an expectation that Siri calls the intents in the block, or doesn’t call them, as the ordering requires.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(_ ordering: Calls.Ordering = .ordered, @IntentExpectationBuilder _ content: () -> [any AppIntentExpectationProviding])
```

## Discussion

The following shows how you can use the builder syntax:

```swift
Calls {
    CreateEventIntent.expect(title: .equals("The expected title"))
}
```

## See Also

### Creating a call expectation
- [enum IntentExpectationBuilder](../intentexpectationbuilder.md)
  A result builder that collects the intents in a calls expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/calls/init(_:_:))*