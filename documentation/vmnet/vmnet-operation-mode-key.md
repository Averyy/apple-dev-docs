# vmnet_operation_mode_key

**Framework**: vmnet  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_operation_mode_key: UnsafePointer<CChar>
```

#### Discussion

The mode in which the guest operating system network interface is configured.

The supported modes are defined at `vmnet`.

The value specified for this key should be of type doc://com.apple.documentation/documentation/xpc/xpc_type_uint64.

## See Also

- [let vmnet_interface_id_key: UnsafePointer<CChar>](vmnet_interface_id_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_operation_mode_key)*