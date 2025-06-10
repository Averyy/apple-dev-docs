# transmitRealtimePackets

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.13.1+ - Deprecated in 10.15.4

## Declaration

```swift
virtual IOReturn transmitRealtimePackets(uint32_t queueIndex, IOEthernetAVBPacket **packets, uint32_t packetCount, bool commonTimestamp, uint32_t *successfulPacketCount);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetcontroller/2934777-transmitrealtimepackets)*