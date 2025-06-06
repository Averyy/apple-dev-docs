# interaction(_:didChangeWith:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Called when the spring-loaded interaction state has changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func interaction(_ interaction: UISpringLoadedInteraction, didChangeWith context: any UISpringLoadedInteractionContext)
```

## Parameters

- `interaction`: The spring-loaded interaction providing the state change information.
- `context`: An object that provides information about the current spring-loaded state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffect/interaction(_:didchangewith:))*