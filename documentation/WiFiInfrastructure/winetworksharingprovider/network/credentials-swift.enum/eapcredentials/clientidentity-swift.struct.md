# WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

A structure that represents the client’s identity.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct ClientIdentity
```

## Topics

### Instance Properties
- [let certificate: Data](./clientidentity-swift.struct/certificate.md)
  The client’s certificate.
- [let certificateChain: [Data]](./clientidentity-swift.struct/certificatechain.md)
  The certificate chain of the client.
- [let privateKey: Data](./clientidentity-swift.struct/privatekey.md)
  The private key of the client.

## Relationships

### Conforms To
- [Decodable](../../../../../Swift/decodable.md)
- [Encodable](../../../../../Swift/encodable.md)
- [Equatable](../../../../../Swift/equatable.md)
- [Hashable](../../../../../Swift/hashable.md)
- [Sendable](../../../../../Swift/sendable.md)
- [SendableMetatype](../../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/clientidentity-swift.struct)*