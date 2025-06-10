# XPCRichError

**Framework**: XPC  
**Kind**: struct

An error that contains a description and indicates if you can retry the operation that caused the error.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
struct XPCRichError
```

## Topics

### Error properties
- [var canRetry: Bool](xpcricherror/canretry.md)
  A Boolean that indicates whether you can retry the operation that caused the error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var XPC_TYPE_RICH_ERROR: xpc_type_t](xpc_type_rich_error-swift.var.md)
  A type that represents a rich error object.
- [var XPC_TYPE_ERROR: xpc_type_t](xpc_type_error-swift.var.md)
  A type that represents an error object.
- [let XPC_ERROR_KEY_DESCRIPTION: UnsafePointer<CChar>](xpc_error_key_description-swift.var.md)
  A key for querying an error dictionary to retrieve a string with a human-readable description of the error.
- [var XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT: xpc_object_t](xpc_error_peer_code_signing_requirement-swift.var.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcricherror)*