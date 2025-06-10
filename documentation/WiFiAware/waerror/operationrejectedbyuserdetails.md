# WAError.OperationRejectedByUserDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details describing the reason a person rejected the operation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct OperationRejectedByUserDetails
```

## Topics

### Initializers - generated
- [init(from: any Decoder) throws](waerror/operationrejectedbyuserdetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties - generated
- [let reason: WAError.OperationRejectedByUserDetails.Reason](waerror/operationrejectedbyuserdetails/reason-swift.property.md)
  The reason why a person rejected the requested operation.
### Enumerations - generated
- [WAError.OperationRejectedByUserDetails.Reason](waerror/operationrejectedbyuserdetails/reason-swift.enum.md)
  The reasons why a person may reject an operation.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/operationrejectedbyuserdetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case operationRejectedByUser(WAError.OperationRejectedByUserDetails)](waerror/operationrejectedbyuser(_:).md)
  An error that occurs if a person denies the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/operationrejectedbyuserdetails)*