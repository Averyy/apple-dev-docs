# sendEvent(_:)

**Framework**: UIKit  
**Kind**: method

Dispatches the specified event to its views.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func sendEvent(_ event: UIEvent)
```

#### Discussion

The [`UIApplication`](uiapplication.md) object calls this method to dispatch events to the window. Window objects dispatch touch events to the view in which the touch occurred, and dispatch other types of events to the most appropriate target object. You can call this method as needed in your app to dispatch custom events that you create. For example, you might call this method to dispatch a custom event to the window’s responder chain.

## Parameters

- `event`: The event to dispatch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/sendevent(_:))*