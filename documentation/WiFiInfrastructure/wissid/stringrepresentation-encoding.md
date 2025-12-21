# stringRepresentation(encoding:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: method

Converts the SSID’s raw data to a string representation using the specified encoding.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func stringRepresentation(encoding: String.Encoding = .utf8) -> String?
```

#### Return Value

A string representation of the SSID, or `nil` if the raw data can’t be converted using the specified encoding.

#### Discussion

Use this method to obtain a human-readable version of the network name. Because SSIDs don’t have a standardized text encoding, the conversion may fail if the raw data can’t be represented as text in the specified encoding.

> ⚠️ **Warning**: Per the Wi-Fi standard, the SSID is a value between 1 and 32 bytes long, and not a `String`. No standard encoding is defined, and any byte value may appear, including embedded NULL characters, control characters, and other unprintable values.

## Parameters

- `encoding`: The text encoding to use for conversion. Defaults to UTF-8.

## See Also

- [init?(String, encoding: String.Encoding)](wissid/init(_:encoding:).md)
  Creates an SSID from a text string using the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wissid/stringrepresentation(encoding:))*