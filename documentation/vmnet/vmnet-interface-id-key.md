# vmnet_interface_id_key

**Framework**: Vmnet  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
var vmnet_interface_id_key: UnsafePointer<CChar>
```

#### Discussion

Interface identifier of the previously created interface.

If no interface identifier is passed to the `vmnet` function, a new MAC address is generated and a interface identifier is associated to it. This identifier is passed back to the client in the `interface_param` dictionary. To re-use a previously generated MAC address, the interface identifier associated with the MAC address needs to be passed to the `vmnet` function in the `interface_desc` parameter.

The value specified for this key should be of type doc://com.apple.documentation/documentation/xpc/xpc_type_uuid.

> ❗ **Important**: Specifying a value for `vmnet_interface_id_key` does not guarantee the return of MAC address associated with the identifier. In cases where the MAC address associated with the id cannot be granted, an error is returned to the caller.

Specifying a value for `vmnet_interface_id_key` does not guarantee the return of MAC address associated with the identifier. In cases where the MAC address associated with the id cannot be granted, an error is returned to the caller.

> **Note**: This key may also be used in an XPC dictionary for a `interface_param` argument, for which it represents the identifier mapping to the MAC address returned in `vmnet_mac_address_key`. See [`interface_param XPC Dictionary Keys`](interface_param_xpc_dictionary_keys.md) for more information.

This key may also be used in an XPC dictionary for a `interface_param` argument, for which it represents the identifier mapping to the MAC address returned in `vmnet_mac_address_key`. See [`interface_param XPC Dictionary Keys`](interface_param_xpc_dictionary_keys.md) for more information.

## See Also

- [var vmnet_operation_mode_key: UnsafePointer<CChar>](vmnet_operation_mode_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_interface_id_key)*