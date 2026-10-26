# kIONetworkFeatureSoftwareVlan

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
kIONetworkFeatureSoftwareVlan = 0x004
```

#### Discussion

Set this bit in the value returned by getFeatures() to indicate that the controller can support software based vlan by transmitting and receiving packets 4 bytes longer that normal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1551508-network/kionetworkfeaturesoftwarevlan)*