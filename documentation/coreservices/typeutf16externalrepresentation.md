# typeUTF16ExternalRepresentation

**Framework**: Core Services  
**Kind**: data  
**Role**: Global Variable

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
var typeUTF16ExternalRepresentation: DescType { get }
```

## Discussion

Unicode text in 16-bit external representation with byte-order-mark (BOM).

Guarantees that either there is a BOM or the data is in UTF-16BE.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/typeutf16externalrepresentation)*