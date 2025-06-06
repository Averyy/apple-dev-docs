# xpc_session_send_message_with_reply_async(_:_:_:)

**Framework**: Xpc  
**Kind**: func

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func xpc_session_send_message_with_reply_async(_ session: any OS_xpc_object, _ message: xpc_object_t, _ reply_handler: @escaping xpc_session_reply_handler_t)
```

## See Also

- [typealias xpc_rich_error_t](xpc_rich_error_t.md)
  A type that describes an error, and whether you can retry the operation that experienced the error.
- [func xpc_rich_error_can_retry(xpc_rich_error_t) -> Bool](xpc_rich_error_can_retry(_:).md)
  Returns a Boolean that indicates whether you can retry the operation that experienced an error.
- [func xpc_rich_error_copy_description(xpc_rich_error_t) -> UnsafeMutablePointer<CChar>?](xpc_rich_error_copy_description(_:).md)
  Copies the string description of an error.
- [func xpc_session_send_message(any OS_xpc_object, xpc_object_t) -> xpc_rich_error_t?](xpc_session_send_message(_:_:).md)
- [typealias xpc_session_reply_handler_t](xpc_session_reply_handler_t-2hf7c.md)
- [func xpc_session_send_message_with_reply_sync(any OS_xpc_object, xpc_object_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> xpc_object_t?](xpc_session_send_message_with_reply_sync(_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_send_message_with_reply_async(_:_:_:))*