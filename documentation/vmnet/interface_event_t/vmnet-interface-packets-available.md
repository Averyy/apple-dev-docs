# VMNET_INTERFACE_PACKETS_AVAILABLE

**Framework**: vmnet  
**Kind**: property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

## Declaration

```swift
static var VMNET_INTERFACE_PACKETS_AVAILABLE: interface_event_t { get }
```

#### Discussion

Event indicating packets are available to be read on the interface.

The `event` dictionary passed in the callback returns the estimated number of packets available to be read using the [`vmnet_estimated_packets_available_key`](vmnet_estimated_packets_available_key.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/interface_event_t/vmnet_interface_packets_available)*