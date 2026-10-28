# XPC_TYPE_ERROR

**Framework**: XPC  
**Kind**: macro  
**Role**: Macro

A type that represents an error object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define XPC_TYPE_ERROR
```

## Discussion

Errors in XPC are dictionaries, but [`xpc_get_type(_:)`](./xpc_get_type%28_%29.md) will return this type when given an error object. You cannot create an error object directly; XPC will only give them to handlers. These error objects have pointer values that are constant across the lifetime of your process and can be safely compared.

These constants are enumerated in the header for the connection object. Error dictionaries may reserve keys so that they can be queried to obtain more detailed information about the error. Currently, the only reserved key is [`XPC_ERROR_KEY_DESCRIPTION`](./xpc_error_key_description-swift.var.md).

## See Also

### Errors
- [XPC_ERROR_KEY_DESCRIPTION](./xpc_error_key_description-c.macro.md)
  A key for querying an error dictionary to retrieve a string with a human-readable description of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_type_error-c.macro)*