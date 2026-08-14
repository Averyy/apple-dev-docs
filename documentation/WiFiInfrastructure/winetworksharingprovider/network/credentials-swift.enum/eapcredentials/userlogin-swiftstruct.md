# WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A person’s login information.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct UserLogin
```

#### Discussion

The framework uses the login information for PEAP, EAP-TTLS, and EAP-FAST. It’s optional for EAP-TLS.

## Topics

### Login credentials
- [let password: String?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/userlogin-swift.struct/password.md)
  The password a person uses to login.
- [let username: String](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/userlogin-swift.struct/username.md)
  Username used to login.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/userlogin-swift.struct)*