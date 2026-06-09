# vmnet_mtu_key

**Framework**: vmnet  
**Kind**: var

The maximum transmission unit (MTU) to configure on the virtual interface in the guest operating system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_mtu_key: UnsafePointer<CChar>
```

#### Discussion

The value for this key is of type [`XPC_TYPE_UINT64`](https://developer.apple.com/documentation/XPC/XPC_TYPE_UINT64-swift.var).

## See Also

- [let vmnet_mac_address_key: UnsafePointer<CChar>](vmnet_mac_address_key.md)
  The MAC address to configure on the virtual interface in the guest operating system.
- [let vmnet_max_packet_size_key: UnsafePointer<CChar>](vmnet_max_packet_size_key.md)
  The maximum size of the packet that an app can write to the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_mtu_key)*