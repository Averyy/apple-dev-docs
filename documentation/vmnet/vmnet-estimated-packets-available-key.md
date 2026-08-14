# vmnet_estimated_packets_available_key

**Framework**: vmnet  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
let vmnet_estimated_packets_available_key: UnsafePointer<CChar>
```

#### Discussion

The estimated number of packets available to be read.

This key is used for the `vmnet` event.

The value for this key is of type [`XPC_TYPE_UINT64`](https://developer.apple.com/documentation/xpc/xpc_type_uint64-swift.var).


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/vmnet_estimated_packets_available_key)*