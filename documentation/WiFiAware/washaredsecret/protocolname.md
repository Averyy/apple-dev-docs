# WASharedSecret.ProtocolName

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

An object that uniquely identifies a particular network protocol and the pairing hanshake it uses for authentication.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct ProtocolName
```

## Topics

### Initializers
- [init?(Data)](./protocolname/init%28_%29-648hd.md)
  Creates a custom protocol with the provided unique string.
- [init?(String)](./protocolname/init%28_%29-7marr.md)
  Creates a custom protocol name using the provided unique string.
### Type Properties
- [static let ipsecPSK: WASharedSecret.ProtocolName](./protocolname/ipsecpsk.md)
  Derive a shared secret to bootstrap IPSec, using the resulting shared secret as the IPSec Pre-Shared Key.
- [static let tlsPSK: WASharedSecret.ProtocolName](./protocolname/tlspsk.md)
  Derive a shared secret to bootstrap TLS, using the resulting shared secret as a TLS Pre-Shared Key.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/protocolname)*