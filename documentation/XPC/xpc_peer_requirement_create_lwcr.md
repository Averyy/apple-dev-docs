# xpc_peer_requirement_create_lwcr

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
extern xpc_peer_requirement_txpc_peer_requirement_create_lwcr(xpc_object_t lwcr, xpc_rich_error_t*error_out);
```

#### Return Value

On success this returns a new peer requirement object. On failure this will return NULL and if set, error_out will be set to an error describing the failure.

#### Discussion

Create a requirement that the peer has the specified lightweight code requirement

This function will return NULL promptly if the lightweight code requirement is invalid.

The lightweight code requirement must be an `xpc_dictionary_t` equivalent of an LWCR constraint (see https://developer.apple.com/documentation/security/defining_launch_environment_and_library_constraints for details on the contents of the dictionary)

The lightweight code requirement in the example below uses the $or operator to require that an executable’s either signed with the Team ID 8XCUU22SN2, or is an operating system executable:

```c
xpc_object_t or_val = xpc_dictionary_create_empty();
xpc_dictionary_set_string(or_val, "team-identifier", "8XCUU22SN2");
xpc_dictionary_set_int64(or_val, "validation-category", 1);

xpc_object_t lwcr = xpc_dictionary_create_empty();
xpc_dictionary_set_value(lwcr, "$or", or_val);

xpc_peer_requirement_t req = xpc_peer_requirement_create_lwcr(lwcr, NULL);
```

## Parameters

- `lwcr`: The lightweight code requirement the peer must have. It is safe to deallocate the lightweight code requirement object after calling this function.
- `error_out`: An out-parameter that, if set and in the event of an error, will point to an {@link xpc_rich_error_t} describing the details of any errors that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_peer_requirement_create_lwcr)*