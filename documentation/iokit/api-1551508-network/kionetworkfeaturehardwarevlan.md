# kIONetworkFeatureHardwareVlan

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
kIONetworkFeatureHardwareVlan = 0x002
```

## Discussion

Set this bit in the value returned by getFeatures() to indicate the controller supports hardware stripping and stuffing of 802.1q vlan tags. If the controller supports this feature it must enable it when initializing so that all received packets delivered to higher layers have the tag stripped. The controller should use setVlanTag() to provide the tag information out of band.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1551508-network/kionetworkfeaturehardwarevlan)*