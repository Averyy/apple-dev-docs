# MLDSA65.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

The public key for MLDSA65.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](mldsa65/publickey/init(rawrepresentation:).md)
  Parses a public key from a serialized representation.
### Getting the raw representation
- [var rawRepresentation: Data](mldsa65/publickey/rawrepresentation.md)
  A serialized representation of the public key.
### Instance Methods
- [func isValidSignature<S, D>(S, for: D) -> Bool](mldsa65/publickey/isvalidsignature(_:for:).md)
  Verifies a MLDSA65 signature.
- [func isValidSignature<S, D, C>(S, for: D, context: C) -> Bool](mldsa65/publickey/isvalidsignature(_:for:context:).md)
  Verifies a MLDSA65 signature, in a specific context.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLDSA65.PrivateKey](mldsa65/privatekey.md)
  The private key for MLDSA65.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/publickey)*