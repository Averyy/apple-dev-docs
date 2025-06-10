# XPC_EVENT_KEY_NAME

**Framework**: XPC  
**Kind**: var

A key for querying an XPC event dictionary to retrieve a string that identifies the event.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
(unsafe) let XPC_EVENT_KEY_NAME: UnsafePointer<CChar>
```

## See Also

- [func xpc_set_event_stream_handler(UnsafePointer<CChar>, dispatch_queue_t?, (xpc_object_t) -> Void)](xpc_set_event_stream_handler(_:_:_:).md)
  Sets the event handler to invoke when receiving streamed events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_event_key_name-swift.var)*