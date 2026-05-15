# init(x963Representation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-256 private key for signing from an ANSI x9.63 representation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init<Bytes>(x963Representation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `x963Representation`: An ANSI x9.63 representation of the key.

## See Also

- [init<Bytes>(rawRepresentation: Bytes) throws](p256/signing/privatekey/init(rawrepresentation:).md)
  Creates a P-256 private key for signing from a collection of bytes.
- [init(compactRepresentable: Bool)](p256/signing/privatekey/init(compactrepresentable:).md)
  Creates a random P-256 private key for signing.
- [init<Bytes>(derRepresentation: Bytes) throws](p256/signing/privatekey/init(derrepresentation:).md)
  Creates a P-256 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p256/signing/privatekey/init(pemrepresentation:).md)
  Creates a P-256 private key for signing from a Privacy-Enhanced Mail PEM) representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/signing/privatekey/init(x963representation:))*