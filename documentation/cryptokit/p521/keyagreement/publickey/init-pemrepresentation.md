# init(pemRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-521 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(pemRepresentation: String) throws
```

## Parameters

- `pemRepresentation`: A PEM representation of the key.

## See Also

- [init<D>(rawRepresentation: D) throws](p521/keyagreement/publickey/init(rawrepresentation:).md)
  Creates a P-521 public key for key agreement from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](p521/keyagreement/publickey/init(compactrepresentation:).md)
  Creates a P-521 public key for key agreement from a compact representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](p521/keyagreement/publickey/init(derrepresentation:).md)
  Creates a P-521 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init<Bytes>(x963Representation: Bytes) throws](p521/keyagreement/publickey/init(x963representation:).md)
  Creates a P-521 public key for key agreement from an ANSI x9.63 representation.
- [init<Bytes>(compressedRepresentation: Bytes) throws](p521/keyagreement/publickey/init(compressedrepresentation:).md)
  Creates a P-521 public key for key agreement from a compressed representation of the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/publickey/init(pemrepresentation:))*