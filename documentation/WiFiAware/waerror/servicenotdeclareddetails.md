# WAError.ServiceNotDeclaredDetails

**Framework**: Wi-Fi Aware  
**Kind**: struct

The optional details that describe the app service wasn’t declared.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ServiceNotDeclaredDetails
```

## Topics

### Generating initializers
- [init(from: any Decoder) throws](waerror/servicenotdeclareddetails/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/servicenotdeclareddetails/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case serviceNotDeclared(WAError.ServiceNotDeclaredDetails)](waerror/servicenotdeclared(_:).md)
  An error that occurs if your app didn’t declared the necessary services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicenotdeclareddetails)*