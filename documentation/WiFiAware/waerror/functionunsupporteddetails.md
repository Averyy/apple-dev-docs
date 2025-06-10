# WAError.FunctionUnsupportedDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing what’s unsupported.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct FunctionUnsupportedDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/functionunsupporteddetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/functionunsupporteddetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case functionUnsupported(WAError.FunctionUnsupportedDetails)](waerror/functionunsupported(_:).md)
  An error that occurs if the system doesn’t support a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/functionunsupporteddetails)*