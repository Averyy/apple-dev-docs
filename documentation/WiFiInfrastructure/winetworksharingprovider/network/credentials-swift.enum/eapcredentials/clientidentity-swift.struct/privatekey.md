# privateKey

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The private key of the client.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
let privateKey: Data
```

#### Discussion

Data will be in PKCS #1 format for an RSA key or ANSI X9.63 format for an EC key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/clientidentity-swift.struct/privatekey)*