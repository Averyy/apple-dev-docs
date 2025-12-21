# init(_:encoding:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates an SSID from a text string using the specified encoding.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
init?(_ ssid: String, encoding: String.Encoding = .utf8)
```

#### Return Value

A new SSID, or `nil` if the string can’t be encoded or results in invalid data length.

#### Discussion

Use this initializer to create SSIDs from human-readable network names. The method converts the string to binary data using the specified encoding before validating against length requirements.

## Parameters

- `ssid`: The network name as a string.
- `encoding`: The text encoding to use for conversion. Defaults to UTF-8.

## See Also

- [func stringRepresentation(encoding: String.Encoding) -> String?](wissid/stringrepresentation(encoding:).md)
  Converts the SSID’s raw data to a string representation using the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wissid/init(_:encoding:))*