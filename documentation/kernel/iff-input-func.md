# iff_input_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*iff_input_func)(void *cookie, ifnet_t interface, protocol_family_t protocol, mbuf_t *data, char **frame_ptr);
```

#### Return_value

Return: 0 - The caller will continue with normal processing of the packet. EJUSTRETURN - The caller will stop processing the packet, the packet will not be freed. Anything Else - The caller will free the packet and stop processing.

#### Discussion

iff_input_func is used to filter incoming packets. The interface is only valid for the duration of the filter call. If you need to keep a reference to the interface, be sure to call ifnet_reference and ifnet_release. The packets passed to the inbound filter are different from those passed to the outbound filter. Packets to the inbound filter have the frame header passed in separately from the rest of the packet. The outbound data filters is passed the whole packet including the frame header.

The frame header usually preceeds the data in the mbuf. This ensures that the frame header will be a valid pointer as long as the mbuf is not freed. If you need to change the frame header to point somewhere else, the recommended method is to prepend a new frame header to the mbuf chain (mbuf_prepend), set the header to point to that data, then call mbuf_adj to move the mbuf data pointer back to the start of the packet payload.

## Parameters

- `cookie`: The cookie specified when this filter was attached.
- `interface`: The interface the packet was recieved on.
- `protocol`: The protocol of this packet. If you specified a protocol when attaching your filter, the protocol will only ever be the protocol you specified.
- `data`: The inbound packet, after the frame header as determined by the interface.
- `frame_ptr`: A pointer to the pointer to the frame header. The frame header length can be found by inspecting the interface's frame header length (ifnet_hdrlen).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iff_input_func)*