# usePAC

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A Boolean value that indicates whether the device uses an existing Protected Access Credential (PAC).

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
let usePAC: Bool
```

#### Discussion

If `true`, the device uses an existing PAC if it’s present. Otherwise, the server must present its identity using a certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/fastconfiguration-swift.struct/usepac)*