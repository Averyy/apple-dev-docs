# kIOEthernetWakeOnPacketAddressMatch

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
kIOEthernetWakeOnPacketAddressMatch = 0x00000002
```

#### Discussion

Reception of a packet which passes through any of the address filtering mechanisms based on its destination Ethernet address. This may include unicast, broadcast, or multicast addresses depending on the current state and setting of the corresponding packet filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1519759-wake_on_lan_filters/kioethernetwakeonpacketaddressmatch)*