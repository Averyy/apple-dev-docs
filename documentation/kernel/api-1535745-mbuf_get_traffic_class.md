# mbuf_get_traffic_class

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.4

## Declaration

```c
mbuf_traffic_class_t mbuf_get_traffic_class(mbuf_t mbuf);
```

#### Return Value

The traffic class

#### Discussion

Get the traffic class of an mbuf packet

## Parameters

- `mbuf`: The mbuf to get the traffic class of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1535745-mbuf_get_traffic_class)*