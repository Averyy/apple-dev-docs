# kIONetworkFeatureSoftwareVlan

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIONetworkFeatureSoftwareVlan = 0x004
```

#### Discussion

Set this bit in the value returned by getFeatures() to indicate that the controller can support software based vlan by transmitting and receiving packets 4 bytes longer that normal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturesoftwarevlan)*