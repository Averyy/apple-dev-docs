# init()

**Framework**: Apple CryptoKit  
**Kind**: init

Initializes a random private key.

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
init() throws
```

## See Also

- [static func generate() throws -> MLKEM1024.PrivateKey](mlkem1024/privatekey/generate.md)
  Generates a new, random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mlkem1024/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM1024.PublicKey?) throws](mlkem1024/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from a seed representation and optional public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/init())*