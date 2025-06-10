# XPC events

**Framework**: XPC

Respond on demand to IOKit events and notifications.

## Topics

### Event handling
- [func xpc_set_event_stream_handler(UnsafePointer<CChar>, dispatch_queue_t?, (xpc_object_t) -> Void)](xpc_set_event_stream_handler(_:_:_:).md)
  Sets the event handler to invoke when receiving streamed events.
- [let XPC_EVENT_KEY_NAME: UnsafePointer<CChar>](xpc_event_key_name-swift.var.md)
  A key for querying an XPC event dictionary to retrieve a string that identifies the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc-events)*