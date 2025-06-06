# shouldAllow(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that determines whether spring-loaded interaction should begin or should continue for the specified context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func shouldAllow(_ interaction: UISpringLoadedInteraction, with context: any UISpringLoadedInteractionContext) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the spring-loaded interaction should begin or continue; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `interaction`: The spring-loaded interaction requesting the information.
- `context`: An object that provides information about the current drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractionbehavior/shouldallow(_:with:))*