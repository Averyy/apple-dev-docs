# wifiAwareServiceRole

**Framework**: AccessorySetupKit  
**Kind**: property

The role of the accessory’s Wi-Fi Aware’s service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var wifiAwareServiceRole: ASDiscoveryDescriptor.WiFiAwareServiceRole { get set }
```

#### Discussion

This property defaults to [`ASDiscoveryDescriptor.WiFiAwareServiceRole.subscriber`](asdiscoverydescriptor/wifiawareservicerole-swift.enum/subscriber.md)

## See Also

- [var wifiAwareServiceName: String?](asdiscoverydescriptor/wifiawareservicename.md)
  The accessory’s Wi-Fi Aware’s service name if available.
- [ASDiscoveryDescriptor.WiFiAwareServiceRole](asdiscoverydescriptor/wifiawareservicerole-swift.enum.md)
  A type that defines the role of an accessory’s Wi-Fi Aware’s service.
- [var wifiAwareModelNameMatch: ASPropertyCompareString?](asdiscoverydescriptor/wifiawaremodelnamematch.md)
  The accessory’s Wi-Fi Aware model name and matching options.
- [var wifiAwareVendorNameMatch: ASPropertyCompareString?](asdiscoverydescriptor/wifiawarevendornamematch.md)
  The accessory’s Wi-Fi Aware vendor name and matching options.
- [class ASPropertyCompareString](aspropertycomparestring.md)
  A type that specifies how to filter a property against a given string and comparison options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/wifiawareservicerole-swift.property)*