# TCP/IP

**Framework**: Kernel  
**Kind**: enum

TCP/IP checksums that may be supported by the hardware.

## Declaration

```c
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

## Overview

Checksums

## Topics

### Constants
- [kChecksumFamilyTCPIP](./tcp_ip/kchecksumfamilytcpip.md)
- [kChecksumIP](./tcp_ip/kchecksumip.md)
- [kChecksumTCP](./tcp_ip/kchecksumtcp.md)
- [kChecksumUDP](./tcp_ip/kchecksumudp.md)
- [kChecksumTCPIPv6](./tcp_ip/kchecksumtcpipv6.md)
- [kChecksumUDPIPv6](./tcp_ip/kchecksumudpipv6.md)
- [kChecksumTCPNoPseudoHeader](./tcp_ip/kchecksumtcpnopseudoheader.md)
- [kChecksumUDPNoPseudoHeader](./tcp_ip/kchecksumudpnopseudoheader.md)
- [kChecksumTCPSum16](./tcp_ip/kchecksumtcpsum16.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkcontroller/tcp_ip)*