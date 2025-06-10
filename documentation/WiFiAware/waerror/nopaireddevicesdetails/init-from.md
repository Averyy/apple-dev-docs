# init(from:)

**Framework**: Wi-Fi Aware  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/nopaireddevicesdetails/init(from:))*