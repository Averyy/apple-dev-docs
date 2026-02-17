# init(_:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Create a MAC Address from the provided octet components.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
init?(_ macAddressComponents: [UInt8])
```

#### Return Value

The mac address, or `nil` if the input data was invalid and it could not be constructed.

## Parameters

- `macAddressComponents`: The native value for the MAC Address in octet components, as defined in the standard.

## See Also

- [var components: [UInt8]](wimacaddress/components.md)
  The MAC Address as a list of octets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/init(_:)-9xhxx)*