# mbuf_is_traffic_class_privileged

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
int mbuf_is_traffic_class_privileged(mbuf_t mbuf);
```

#### Return_value

Non-zero if privileged, 0 otherwise.

#### Discussion

Returns the privileged status of the traffic class of the packet specified by the mbuf.

## Parameters

- `mbuf`: The mbuf to retrieve the status from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535772-mbuf_is_traffic_class_privileged)*