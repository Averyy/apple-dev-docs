# vmnet_max_packet_size_key

**Framework**: vmnet  
**Kind**: var

The maximum size of the packet that an app can write to the interface.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_max_packet_size_key: UnsafePointer<CChar>
```

#### Discussion

This also defines the minimum size of the packet an app needs to be pass to the `vmnet` function for a successful read.

The value for this key is of type [`XPC_TYPE_UINT64`](https://developer.apple.com/documentation/xpc/xpc_type_uint64-swift.var).

## See Also

- [let vmnet_mac_address_key: UnsafePointer<CChar>](vmnet_mac_address_key.md)
  The MAC address to configure on the virtual interface in the guest operating system.
- [let vmnet_mtu_key: UnsafePointer<CChar>](vmnet_mtu_key.md)
  The maximum transmission unit (MTU) to configure on the virtual interface in the guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_max_packet_size_key)*