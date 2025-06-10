# WAError.OperationNotPermittedDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing what isn’t permitted.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct OperationNotPermittedDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/operationnotpermitteddetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/operationnotpermitteddetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case operationNotPermitted(WAError.OperationNotPermittedDetails)](waerror/operationnotpermitted(_:).md)
  An error that occurs if an operation isn’t permitted by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/operationnotpermitteddetails)*