# init(_:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates a MAC Address from the provided case-insensitive string, of the format `"XX:XX:XX:XX:XX:XX"`.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init?(_ macAddress: String)
```

#### Return Value

The mac address, or `nil` if the input data was invalid and it could not be constructed.

## Parameters

- `macAddress`: The BSSID as a String.

## See Also

- [var stringRepresentation: String](wimacaddress/stringrepresentation.md)
  The MAC Address as an uppercase string, in the format `"XX:XX:XX:XX:XX:XX"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress/init(_:)-7kdi9)*