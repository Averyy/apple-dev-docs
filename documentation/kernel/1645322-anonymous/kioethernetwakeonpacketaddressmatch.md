# kIOEthernetWakeOnPacketAddressMatch

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIOEthernetWakeOnPacketAddressMatch = 0x00000002
```

#### Discussion

Reception of a packet which passes through any of the address filtering mechanisms based on its destination Ethernet address. This may include unicast, broadcast, or multicast addresses depending on the current state and setting of the corresponding packet filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645322-anonymous/kioethernetwakeonpacketaddressmatch)*