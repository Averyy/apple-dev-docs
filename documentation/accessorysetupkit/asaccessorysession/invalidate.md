# invalidate()

**Framework**: AccessorySetupKit  
**Kind**: method

Invalidate the session by stopping any operations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

This call breaks any retain cycles. The session is unusable after calling `invalidate`.

## See Also

- [func activate(on: dispatch_queue_t, eventHandler: (ASAccessoryEvent) -> Void)](asaccessorysession/activate(on:eventhandler:).md)
  Activate the session and start delivering events to an event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/invalidate())*