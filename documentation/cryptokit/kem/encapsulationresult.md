# KEM.EncapsulationResult

**Framework**: Apple CryptoKit  
**Kind**: struct

The result of a key encapsulation operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct EncapsulationResult
```

## Topics

### Initializers
- [init(sharedSecret: SymmetricKey, encapsulated: Data)](kem/encapsulationresult/init(sharedsecret:encapsulated:).md)
  Initializes a key encapsulation result.
### Instance Properties
- [let encapsulated: Data](kem/encapsulationresult/encapsulated.md)
  The encapsulated representation of the shared secret.
- [let sharedSecret: SymmetricKey](kem/encapsulationresult/sharedsecret.md)
  The shared secret.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kem/encapsulationresult)*