# xpc_set_event_stream_handler(_:_:_:)

**Framework**: XPC  
**Kind**: func

Sets the event handler to invoke when receiving streamed events.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func xpc_set_event_stream_handler(_ stream: UnsafePointer<CChar>, _ targetq: dispatch_queue_t?, _ handler: @escaping (xpc_object_t) -> Void)
```

#### Discussion

Multiple calls to this function for the same event stream will result in undefined behavior.

## Parameters

- `stream`: The name of the event stream for which this handler will be invoked.
- `targetq`: The GCD queue to which the event handler block will be submitted. This parameter may be NULL, in which case the connection’s target queue will be the default target queue of  , defined as  .
- `handler`: The event handler block. The event which this block receives as its first parameter will always be a dictionary which contains the   key. The value for this key will be a string whose value is the name assigned to the XPC event specified in the  . Future keys may be added to this dictionary.

## See Also

- [let XPC_EVENT_KEY_NAME: UnsafePointer<CChar>](xpc_event_key_name-swift.var.md)
  A key for querying an XPC event dictionary to retrieve a string that identifies the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_set_event_stream_handler(_:_:_:))*