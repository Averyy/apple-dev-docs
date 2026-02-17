# vmnet_mtu_key

**Framework**: vmnet  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_mtu_key: UnsafePointer<CChar>
```

#### Discussion

The MTU to be configured on the virtual interface in the guest operating system.

The value for this key is of type [`XPC_TYPE_UINT64`](https://developer.apple.com/documentation/XPC/XPC_TYPE_UINT64-swift.var).

## See Also

- [let vmnet_mac_address_key: UnsafePointer<CChar>](vmnet_mac_address_key.md)
- [let vmnet_max_packet_size_key: UnsafePointer<CChar>](vmnet_max_packet_size_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_mtu_key)*