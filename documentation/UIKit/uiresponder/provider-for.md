# provider(for:)

**Framework**: UIKit  
**Kind**: method

Asks the responder for an element provider to fulfill the given focus-based deferred element. Check the `identifier` of the deferred element to identify which deferred element this is. By default, this returns nil. Return a non-nil `provider` to make this responder responsible for providing elements for this fulfillment of the deferred element.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func provider(for deferredElement: UIDeferredMenuElement) -> UIDeferredMenuElement.Provider?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/provider(for:))*