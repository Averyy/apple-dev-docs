# signature(for:context:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a MLDSA87 signature, with context.

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
func signature<D, C>(for data: D, context: C) throws -> Data where D : DataProtocol, C : DataProtocol
```

#### Return Value

The MLDSA87 signature. This method throws if CryptoKit encounters an error producing the signature.

## Parameters

- `data`: The data to sign.
- `context`: Context for the signature.

## See Also

- [func signature<D>(for: D) throws -> Data](mldsa87/privatekey/signature(for:).md)
  Generates a MLDSA87 signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/signature(for:context:))*