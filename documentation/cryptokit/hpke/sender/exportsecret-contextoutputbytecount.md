# exportSecret(context:outputByteCount:)

**Framework**: Apple CryptoKit  
**Kind**: method

Exports a secret given domain-separation context and the desired output length.

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
func exportSecret<Context>(context: Context, outputByteCount: Int) throws -> SymmetricKey where Context : DataProtocol
```

#### Return Value

The exported secret.

## Parameters

- `context`: Application-specific information providing context on the use of this key.
- `outputByteCount`: The desired length of the exported secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/sender/exportsecret(context:outputbytecount:))*