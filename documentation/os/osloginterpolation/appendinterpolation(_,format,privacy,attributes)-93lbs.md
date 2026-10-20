# appendInterpolation(_:format:privacy:attributes:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Appends an interpolated collection of raw bytes with the specified attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawBufferPointer, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated collection of raw bytes to a log message.

## Parameters

- `pointer`: The interpolated collection of raw bytes. The system automatically wraps this value in a closure.
- `format`: The format to apply to the value when the system renders it in a log message. For more information, see [`OSLogPointerFormat`](../oslogpointerformat.md). The default value is [`OSLogPointerFormat.none`](../oslogpointerformat/none.md).
- `privacy`: The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [`OSLogPrivacy`](../oslogprivacy.md). The default value is [`auto`](../oslogprivacy/auto.md).
- `attributes`: Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## See Also

### Appending Pointer Data
- [func appendInterpolation(@autoclosure () -> UnsafeRawPointer, bytes: @autoclosure () -> Int, format: OSLogPointerFormat, privacy: OSLogPrivacy)](./appendinterpolation%28_,bytes,format,privacy%29.md)
  Appends interpolated pointer data.
- [func appendInterpolation(@autoclosure () -> UnsafeRawPointer, bytes: @autoclosure () -> Int, format: OSLogPointerFormat, privacy: OSLogPrivacy, attributes: String)](./appendinterpolation%28_,bytes,format,privacy,attributes%29.md)
  Appends interpolated pointer data with the specified attributes.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy)](./appendinterpolation%28_,format,privacy%29-5qaau.md)
  Appends an interpolated collection of raw bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs)*