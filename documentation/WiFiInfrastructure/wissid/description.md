# description

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

This property provides a readable representation suitable for logging and debugging.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
var description: String { get }
```

#### Discussion

When the SSID can be converted to UTF-8 text, it displays the text in quotes. Otherwise, it shows the raw bytes as hexadecimal values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wissid/description)*