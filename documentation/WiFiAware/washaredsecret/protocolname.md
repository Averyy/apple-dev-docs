# WASharedSecret.ProtocolName

**Framework**: Wi-Fi Aware  
**Kind**: struct

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
- [init?(Data)](washaredsecret/protocolname/init(_:)-648hd.md)
  Creates a custom protocol with the provided unique string.
- [init?(String)](washaredsecret/protocolname/init(_:)-7marr.md)
  Creates a custom protocol name using the provided unique string.
### Type Properties
- [static let ipsecPSK: WASharedSecret.ProtocolName](washaredsecret/protocolname/ipsecpsk.md)
  Derive a shared secret to bootstrap IPSec, using the resulting shared secret as the IPSec Pre-Shared Key.
- [static let tlsPSK: WASharedSecret.ProtocolName](washaredsecret/protocolname/tlspsk.md)
  Derive a shared secret to bootstrap TLS, using the resulting shared secret as a TLS Pre-Shared Key.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/washaredsecret/protocolname)*