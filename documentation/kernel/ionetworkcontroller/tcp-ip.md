# TCP/IP

**Framework**: Kernel  
**Kind**: enum

TCP/IP checksums that may be supported by the hardware.

## Declaration

```swift
enum {
   kChecksumFamilyTCPIP = 0x00000001,
   kChecksumIP = 0x0001,
   kChecksumTCP = 0x0002,
   kChecksumUDP = 0x0004,
   kChecksumTCPIPv6 = 0x0020,
   kChecksumUDPIPv6 = 0x0040,
   kChecksumTCPNoPseudoHeader = 0x0100,
   kChecksumUDPNoPseudoHeader = 0x0200,
   kChecksumTCPSum16 = 0x1000
};
```

#### Overview

Checksums

## Topics

### Constants
- [kChecksumFamilyTCPIP](ionetworkcontroller/tcp_ip/kchecksumfamilytcpip.md)
- [kChecksumIP](ionetworkcontroller/tcp_ip/kchecksumip.md)
- [kChecksumTCP](ionetworkcontroller/tcp_ip/kchecksumtcp.md)
- [kChecksumUDP](ionetworkcontroller/tcp_ip/kchecksumudp.md)
- [kChecksumTCPIPv6](ionetworkcontroller/tcp_ip/kchecksumtcpipv6.md)
- [kChecksumUDPIPv6](ionetworkcontroller/tcp_ip/kchecksumudpipv6.md)
- [kChecksumTCPNoPseudoHeader](ionetworkcontroller/tcp_ip/kchecksumtcpnopseudoheader.md)
- [kChecksumUDPNoPseudoHeader](ionetworkcontroller/tcp_ip/kchecksumudpnopseudoheader.md)
- [kChecksumTCPSum16](ionetworkcontroller/tcp_ip/kchecksumtcpsum16.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkcontroller/tcp_ip)*