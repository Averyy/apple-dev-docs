# provisionPACAnonymously

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A Boolean value that indicates whether to provision the device anonymously.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
let provisionPACAnonymously: Bool
```

#### Discussion

If `true`, the framework provisions the device anonymously.

> **Note**: There are known machine-in-the-middle attacks that affect anonymous provisioning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/fastconfiguration-swift.struct/provisionpacanonymously)*