# WAError.ErrorDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the error.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ErrorDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/errordetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/errordetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case error(WAError.ErrorDetails)](waerror/error(_:).md)
  A general error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/errordetails)*