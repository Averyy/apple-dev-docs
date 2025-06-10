# WAError.OperationRejectedByUserDetails.Reason

**Framework**: Wi-Fi Aware  
**Kind**: enum

The reasons why a person may reject an operation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum Reason
```

## Topics

### Enumeration Cases - generated
- [WAError.OperationRejectedByUserDetails.Reason.airplaneModeEnabled](waerror/operationrejectedbyuserdetails/reason-swift.enum/airplanemodeenabled.md)
  A person has Airplane Mode enabled.
- [WAError.OperationRejectedByUserDetails.Reason.declined](waerror/operationrejectedbyuserdetails/reason-swift.enum/declined.md)
  A person explicitly declined the operation on the UI.
- [WAError.OperationRejectedByUserDetails.Reason.wifiOff](waerror/operationrejectedbyuserdetails/reason-swift.enum/wifioff.md)
  A person using your app turned Wi-Fi off, or has it off.
### Initializers - generated
- [init(from: any Decoder) throws](waerror/operationrejectedbyuserdetails/reason-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (WAError.OperationRejectedByUserDetails.Reason, WAError.OperationRejectedByUserDetails.Reason) -> Bool](waerror/operationrejectedbyuserdetails/reason-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](waerror/operationrejectedbyuserdetails/reason-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/operationrejectedbyuserdetails/reason-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](waerror/operationrejectedbyuserdetails/reason-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](waerror/operationrejectedbyuserdetails/reason-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/operationrejectedbyuserdetails/reason-swift.enum)*