# minimumTLSVersion

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The oldest version of Transport Layer Security (TLS) that this configuration accepts to authenticate this network.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
let minimumTLSVersion: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.TLSVersion?
```

#### Discussion

This value is `nil` if the configuration doesn’t specify a minimum TLS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct/minimumtlsversion)*