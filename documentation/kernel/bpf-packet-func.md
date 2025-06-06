# bpf_packet_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*bpf_packet_func)(ifnet_t interface, mbuf_t data);
```

#### Return_value

An errno value or zero upon success.

#### Discussion

bpf_packet_func The bpf_packet_func is used to intercept inbound and outbound packets. The tap function will never free the mbuf. The tap function will only copy the mbuf in to various bpf file descriptors tapping this interface.

## Parameters

- `interface`: The interface being sent or received on.
- `data`: The packet to be transmitted or received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/bpf_packet_func)*