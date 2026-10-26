# kIONetworkFeatureTransmitCompletionStatus

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```c
kIONetworkFeatureTransmitCompletionStatus = 0x040
```

#### Discussion

Set this bit to advertise the capability to report per-packet transmit completion status. See `IONetworkInterface::reportTransmitCompletionStatus`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1551508-network/kionetworkfeaturetransmitcompletionstatus)*