# init(from:)

**Framework**: os  
**Kind**: init

Decodes the interval state from the provided decoder.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
required init(from decoder: any Decoder) throws
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the object you’re using to decode the interval state, which must adopt the [`Decoder`](https://developer.apple.com/documentation/Swift/Decoder) protocol, calls it on your behalf as part of the serialization process.

 You don’t call this method directly. Instead, the object you’re using to decode the interval state, which must adopt the [`Decoder`](https://developer.apple.com/documentation/Swift/Decoder) protocol, calls it on your behalf as part of the serialization process.

The initializer throws an error if reading from the decoder fails, or if the decoder’s data is corrupt or invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostintervalstate/init(from:))*