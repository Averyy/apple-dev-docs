# vmnet_operation_mode_key

**Framework**: vmnet  
**Kind**: var

The mode to use to configure the guest operating system network interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_operation_mode_key: UnsafePointer<CChar>
```

#### Discussion

The value specified for this key should be of type [`XPC_TYPE_UINT64`](https://developer.apple.com/documentation/XPC/XPC_TYPE_UINT64-swift.var).

## See Also

- [let vmnet_interface_id_key: UnsafePointer<CChar>](vmnet_interface_id_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_operation_mode_key)*