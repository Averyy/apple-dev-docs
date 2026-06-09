# vmnet_enable_virtio_header_key

**Framework**: vmnet  
**Kind**: var

Enable virtio headers in all packets.

**Availability**:
- Mac Catalyst 13.0+
- macOS 15.4+

## Declaration

```swift
let vmnet_enable_virtio_header_key: UnsafePointer<CChar>
```

#### Discussion

For more information, see [`5.1.6 Device Operation`](https://developer.apple.comhttps://docs.oasis-open.org/virtio/virtio/v1.1/virtio-v1.1.html) in the Virtio specification

You must not specify this property if [`vmnet_enable_checksum_offload_key`](vmnet_enable_checksum_offload_key.md) is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_enable_virtio_header_key-swift.var)*