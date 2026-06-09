# init(_:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Create a MAC Address from the provided data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init?(_ macAddressData: Data)
```

#### Return Value

The mac address, or `nil` if the input data was invalid and it could not be constructed.

## Parameters

- `macAddressData`: The native value for the MAC Address as data.

## See Also

- [let data: Data](wimacaddress/data.md)
  The raw data value of the MAC Address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/init(_:)-6044i)*