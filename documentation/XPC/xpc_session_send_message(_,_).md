# xpc_session_send_message(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: send(message:))
- macOS 13.0+ - Deprecated in 14.0 (renamed: send(message:))

## Declaration

```swift
func xpc_session_send_message(_ session: any OS_xpc_object, _ message: xpc_object_t) -> xpc_rich_error_t?
```

## See Also

### Sending messages
- [typealias xpc_rich_error_t](./xpc_rich_error_t.md)
  A type that describes an error, and whether you can retry the operation that experienced the error.
- [func xpc_rich_error_can_retry(xpc_rich_error_t) -> Bool](./xpc_rich_error_can_retry%28_%29.md)
  Returns a Boolean that indicates whether you can retry the operation that experienced an error.
- [func xpc_rich_error_copy_description(xpc_rich_error_t) -> UnsafeMutablePointer<CChar>?](./xpc_rich_error_copy_description%28_%29.md)
  Copies the string description of an error.
- [func xpc_session_send_message_with_reply_async(any OS_xpc_object, xpc_object_t, xpc_session_reply_handler_t)](./xpc_session_send_message_with_reply_async%28_,_,_%29.md)
- [typealias xpc_session_reply_handler_t](./xpc_session_reply_handler_t-2hf7c.md)
- [func xpc_session_send_message_with_reply_sync(any OS_xpc_object, xpc_object_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> xpc_object_t?](./xpc_session_send_message_with_reply_sync%28_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_send_message(_:_:))*