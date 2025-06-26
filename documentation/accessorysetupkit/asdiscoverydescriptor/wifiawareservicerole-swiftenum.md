# ASDiscoveryDescriptor.WiFiAwareServiceRole

**Framework**: AccessorySetupKit  
**Kind**: enum

A type that defines the role of an accessory’s Wi-Fi Aware’s service.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum WiFiAwareServiceRole
```

## Topics

### Determining service role
- [ASDiscoveryDescriptor.WiFiAwareServiceRole.subscriber](asdiscoverydescriptor/wifiawareservicerole-swift.enum/subscriber.md)
  The subscriber service role.
- [ASDiscoveryDescriptor.WiFiAwareServiceRole.publisher](asdiscoverydescriptor/wifiawareservicerole-swift.enum/publisher.md)
  The publisher service role.
### Working with raw values
- [init?(rawValue: Int)](asdiscoverydescriptor/wifiawareservicerole-swift.enum/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](asdiscoverydescriptor/wifiawareservicerole-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](asdiscoverydescriptor/wifiawareservicerole-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var wifiAwareServiceName: String?](asdiscoverydescriptor/wifiawareservicename.md)
  The accessory’s Wi-Fi Aware’s service name if available.
- [var wifiAwareServiceRole: ASDiscoveryDescriptor.WiFiAwareServiceRole](asdiscoverydescriptor/wifiawareservicerole-swift.property.md)
  The role of the accessory’s Wi-Fi Aware’s service.
- [var wifiAwareModelNameMatch: ASPropertyCompareString?](asdiscoverydescriptor/wifiawaremodelnamematch.md)
  The accessory’s Wi-Fi Aware model name and matching options.
- [var wifiAwareVendorNameMatch: ASPropertyCompareString?](asdiscoverydescriptor/wifiawarevendornamematch.md)
  The accessory’s Wi-Fi Aware vendor name and matching options.
- [class ASPropertyCompareString](aspropertycomparestring.md)
  A type that specifies how to filter a property against a given string and comparison options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/wifiawareservicerole-swift.enum)*