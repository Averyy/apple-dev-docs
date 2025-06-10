# kChecksumUDPNoPseudoHeader

**Framework**: Kernel  
**Kind**: data

#### Overview

A UDP checksum that covers the UDP header and the UDP data, but the pseudo header is not included in the checksum computation. A partial 16-bit checksum value must be provided to allow the protocol stacks to calculate and verify the final checksum. This type of checksum is not currently supported on the output path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkcontroller/tcp_ip/kchecksumudpnopseudoheader)*