# shouldAllow(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that determines whether spring-loaded interaction should begin or should continue for the specified context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func shouldAllow(_ interaction: UISpringLoadedInteraction, with context: any UISpringLoadedInteractionContext) -> Bool
```

```objc
- (BOOL) shouldAllowInteraction:(UISpringLoadedInteraction *) interaction withContext:(id<UISpringLoadedInteractionContext>) context;
```

#### Return Value

[`true`](../../Swift/true.md) if the spring-loaded interaction should begin or continue; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `interaction`: The spring-loaded interaction requesting the information.
- `context`: An object that provides information about the current drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractionbehavior/shouldallow(_:with:))*