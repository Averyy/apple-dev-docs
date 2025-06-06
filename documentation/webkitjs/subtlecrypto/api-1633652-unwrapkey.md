# unwrapKey

**Framework**: Webkitjs  
**Kind**: instm

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
Promise <CryptoKey> unwrapKey(
    KeyFormat format, 
    BufferSource wrappedKey, 
    CryptoKey unwrappingKey, 
    AlgorithmIdentifier unwrapAlgorithm, 
    AlgorithmIdentifier unwrappedKeyAlgorithm, 
    boolean extractable, 
    sequence <KeyUsage> keyUsages
);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/subtlecrypto/1633652-unwrapkey)*