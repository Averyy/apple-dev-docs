# encode(to:)

**Framework**: os  
**Kind**: method

Encodes the interval state into the provided encoder.

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
func encode(to encoder: any Encoder) throws
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the object you’re using to encode the interval state, which must adopt the [`Encoder`](https://developer.apple.com/documentation/Swift/Encoder) protocol, calls it on your behalf as part of the serialization process.

 You don’t call this method directly. Instead, the object you’re using to encode the interval state, which must adopt the [`Encoder`](https://developer.apple.com/documentation/Swift/Encoder) protocol, calls it on your behalf as part of the serialization process.

The method throws an error if the interval state is invalid for the specified encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignpostintervalstate/encode(to:))*