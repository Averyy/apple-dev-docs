# kIONetworkInterfaceDisabledState

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kIONetworkInterfaceDisabledState = 0x4
```

#### Discussion

The interface is temporarily unable to service its clients. This will occur when the network controller that is servicing the interface has entered a low power state that renders it unusable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1579661-interfaceobjectstates/kionetworkinterfacedisabledstate)*