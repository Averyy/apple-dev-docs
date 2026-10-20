# IFNET_TX_STATUS

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.12+

## Declaration

```c
IFNET_TX_STATUS = 0x00800000
```

#### Discussion

Driver supports returning a per packet transmission status (pass, fail or other errors) of whether the packet was successfully transmitted on the link, or the transmission was aborted, or transmission failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_tx_status)*