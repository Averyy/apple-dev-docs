# vmnet_max_packet_size_key

**Framework**: vmnet  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_max_packet_size_key: UnsafePointer<CChar>
```

#### Discussion

The maximum size of the packet that can be written to the interface. This also defines the minimum size of the packet that needs to be passed to the `vmnet` function for a successful read.

The value for this key is of type doc://com.apple.documentation/documentation/xpc/xpc_type_uint64.

## See Also

- [let vmnet_mac_address_key: UnsafePointer<CChar>](vmnet_mac_address_key.md)
- [let vmnet_mtu_key: UnsafePointer<CChar>](vmnet_mtu_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_max_packet_size_key)*