# init(_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates an expectation that Siri surfaces each entity in the block by search or resolution.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(@EntityFindExpectationBuilder _ content: () -> [any AppEntityExpectationProviding])
```

## Discussion

A found entity carries the properties Siri read for it before its next intent ran, from your app’s Spotlight index or from your app. A property Siri never read has no value: a check that needs one fails, and `.isNil` holds on it. A property of the entity itself whose name begins with `_`, or that is named `liveAppEntityFeedId`, is never relayed, so `.isNil` holds on it too.

The following shows how you can use the builder syntax:

```swift
Finds {
    EventEntity.expect(title: .equals("The expected title"))
}
```

## See Also

### Creating a find expectation
- [enum EntityFindExpectationBuilder](../entityfindexpectationbuilder.md)
  A result builder that collects the entities a finds expectation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/finds/init(_:))*