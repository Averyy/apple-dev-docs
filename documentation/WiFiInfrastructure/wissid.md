# WISSID

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

The Service Set Identifier (SSID) for a Wi-Fi network, from which applications derive the human-readable network name.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
struct WISSID
```

#### Overview

An SSID represents the identifier for a wireless network, as the Wi-Fi standard defines. Your app converts this binary data to text when displaying network names to people. The Wi-Fi standard defines SSIDs as binary values between 1 and 32 bytes long, without specifying a text encoding. This means SSID data can include:

- Embedded null bytes (`0x00`)
- Control characters and escape sequences
- Non-printable binary data
- Text in various encodings (UTF-8, ASCII, Latin-1, etc.)
- Mixed binary and text content

Don’t assume SSID data represents UTF-8 encoded text. Use [`stringRepresentation(encoding:)`](wissid/stringrepresentation(encoding:).md) to safely convert the raw data to a readable format. Since no standard encoding exists for SSIDs, different networks may use different text encodings or contain pure binary data. When converting SSIDs to strings:

- Try UTF-8 encoding first, as it’s most common.
- Fall back to other encodings if UTF-8 conversion fails.
- Handle cases where no text representation is possible.
- Consider displaying raw hexadecimal values for non-text SSIDs.

## Topics

### Working with SSIDs as a string
- [init?(String, encoding: String.Encoding)](wissid/init(_:encoding:).md)
  Creates an SSID from a text string using the specified encoding.
- [func stringRepresentation(encoding: String.Encoding) -> String?](wissid/stringrepresentation(encoding:).md)
  Converts the SSID’s raw data to a string representation using the specified encoding.
### Working with raw SSID data
- [init?(Data)](wissid/init(_:).md)
  Creates an SSID from raw binary data.
- [let data: Data](wissid/data.md)
  The raw binary data of the SSID as transmitted over-the-air.
### Getting a description
- [var description: String](wissid/description.md)
  This property provides a readable representation suitable for logging and debugging.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wissid)*