# signature(for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a MLDSA87 signature

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
func signature<D>(for data: D) throws -> Data where D : DataProtocol
```

#### Return Value

The MLDSA87 signature

#### Discussion

> **Note**: If there is a failure producing the signature

## Parameters

- `data`: The data to sign


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa87/privatekey/signature(for:))*