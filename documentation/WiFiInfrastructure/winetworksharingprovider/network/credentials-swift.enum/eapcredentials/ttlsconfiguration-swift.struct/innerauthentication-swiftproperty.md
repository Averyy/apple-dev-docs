# innerAuthentication

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The inner authentication type to use for the Tunneled Transport Layer Security (TTLS) configuration.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
let innerAuthentication: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration.InnerAuthentication?
```

#### Discussion

This value is `nil` if the configuration doesn’t specify an inner authentication type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/ttlsconfiguration-swift.struct/innerauthentication-swift.property)*