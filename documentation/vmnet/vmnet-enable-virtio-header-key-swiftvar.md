# vmnet_enable_virtio_header_key

**Framework**: vmnet  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 15.4+

## Declaration

```swift
let vmnet_enable_virtio_header_key: UnsafePointer<CChar>
```

#### Discussion

Enable virtio headers in all packets.

- see “5.1.6 Device Operation” at https://docs.oasis-open.org/virtio/virtio/v1.1/virtio-v1.1.html This property must not be specified if `vmnet_enable_checksum_offload_key` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_enable_virtio_header_key-swift.var)*