# init(_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates an expectation that each entity in the block is onscreen.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(@OnScreenEntityExpectationBuilder _ content: () -> [any ResolvableAppEntityExpectation])
```

## Discussion

Onscreen entities are identity-based. A staged view shows entities the author already knows, so property matching is not offered here. For property-based matching of search results, see [`Finds`](../finds.md).

The following shows how you can use the builder syntax:

```swift
OnScreen {
    EventEntity.expectIdentifier("An identifier")
}
```

## See Also

### Creating an onscreen expectation
- [enum OnScreenEntityExpectationBuilder](../onscreenentityexpectationbuilder.md)
  A result builder that collects the entities an onscreen expectation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/onscreen/init(_:))*