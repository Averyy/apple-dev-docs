# bpf_tap_out

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
void bpf_tap_out(ifnet_t interface, u_int32_t dlt, mbuf_t packet, void *header, size_t header_len);
```

#### Discussion

Call this function when your interface trasmits a packet. This function will check if any bpf devices need a a copy of the packet.

## Parameters

- `interface`: The interface the packet was or will be transmitted on.
- `dlt`: The data link type of the packet.
- `packet`: The packet received.
- `header`: An optional pointer to a header that will be prepended.
- `headerlen`: If the header was specified, the length of the header.

## See Also

- [bpf_attach](1589700-bpf_attach.md)
- [bpf_tap_in](1589470-bpf_tap_in.md)
- [bpfattach](1589467-bpfattach.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1589576-bpf_tap_out)*