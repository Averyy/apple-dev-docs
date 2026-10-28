# xpc_peer_requirement_create_entitlement_matches_value

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
extern xpc_peer_requirement_txpc_peer_requirement_create_entitlement_matches_value(const char *entitlement, xpc_object_t value, xpc_rich_error_t*error_out);
```

## Return Value

On success this returns a new peer requirement object. On failure this will return NULL and if set, error_out will be set to an error describing the failure.

## Discussion

Create a requirement that the peer has the entitlement with matching value

This function will return NULL promptly if the entitlement requirement is invalid.

## Parameters

- `entitlement`: The entitlement the peer must have. It is safe to deallocate the entitlement string after calling this function.
- `value`: The value that the entitlement must match. It is safe to deallocate the value object after calling this function. Valid xpc types for this object are `XPC_TYPE_BOOL`, `XPC_TYPE_STRING` and `XPC_TYPE_INT64`.
- `error_out`: An out-parameter that, if set and in the event of an error, will point to an {@link xpc_rich_error_t} describing the details of any errors that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_peer_requirement_create_entitlement_matches_value)*