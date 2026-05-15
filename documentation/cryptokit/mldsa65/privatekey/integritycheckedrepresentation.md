# integrityCheckedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property

The integrity-checked data representation of the private key.

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
var integrityCheckedRepresentation: Data { get }
```

#### Discussion

This representation is 64 bytes long, and contains the seed and a hash of the public key.

## See Also

- [var publicKey: MLDSA65.PublicKey](mldsa65/privatekey/publickey.md)
  The associated public key.
- [var seedRepresentation: Data](mldsa65/privatekey/seedrepresentation.md)
  The seed representation of the private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/integritycheckedrepresentation)*