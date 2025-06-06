# mbuf_traffic_class_t

**Framework**: Kernel  
**Kind**: enum

Traffic class of a packet

**Availability**:
- macOS 10.7+

## Declaration

```swift
typedef enum mbuf_traffic_class_t : unsigned int {
    ...
} mbuf_traffic_class_t;
```

#### Overview

Property that represent the category of traffic of a packet. This information may be used by the driver and at the link level.

## Topics

### Constants
- [MBUF_TC_BE](mbuf_traffic_class_t/mbuf_tc_be.md)
- [MBUF_TC_BK](mbuf_traffic_class_t/mbuf_tc_bk.md)
- [MBUF_TC_VI](mbuf_traffic_class_t/mbuf_tc_vi.md)
- [MBUF_TC_VO](mbuf_traffic_class_t/mbuf_tc_vo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/mbuf_traffic_class_t)*