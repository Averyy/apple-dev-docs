# generate()

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a new, random private key.

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
static func generate() throws -> MLKEM768.PrivateKey
```

## See Also

- [init() throws](mlkem768/privatekey/init.md)
  Initializes a random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mlkem768/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws](mlkem768/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from a seed representation and optional public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/generate())*