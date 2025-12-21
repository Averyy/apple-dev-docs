# init(_:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates an SSID from raw binary data.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
init?(_ ssid: Data)
```

#### Return Value

A new SSID, or `nil`if the data length is invalid.

#### Discussion

Use this initializer when working with SSID data received from Wi-Fi enabled accessories. Valid SSIDs conform to Wi-Fi standard length requirements.

## Parameters

- `ssid`: The raw binary data representing the SSID, between 1 and 32 bytes in length.

## See Also

- [let data: Data](wissid/data.md)
  The raw binary data of the SSID as transmitted over-the-air.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/wissid/init(_:))*