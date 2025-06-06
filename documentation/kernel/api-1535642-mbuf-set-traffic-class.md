# mbuf_set_traffic_class

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```swift
errno_t mbuf_set_traffic_class(mbuf_t mbuf, mbuf_traffic_class_t tc);
```

#### Return_value

0 on success, EINVAL if bad parameter is passed

#### Discussion

Set the traffic class of an mbuf packet.

## Parameters

- `mbuf`: The mbuf to set the traffic class on. @tc The traffic class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535642-mbuf_set_traffic_class)*