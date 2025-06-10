# if_input_poll

**Framework**: Kernel  
**Kind**: clm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static void if_input_poll(ifnet_t ifp, uint32_t flags, uint32_t max_count, mbuf_t *first_packet, mbuf_t *last_packet, uint32_t *cnt, uint32_t *len);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkinterface/1503003-if_input_poll)*