# appendInterpolation(_:bytes:format:privacy:attributes:)

**Framework**: os  
**Kind**: method

Appends interpolated pointer data with the specified attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawPointer, bytes: @autoclosure @escaping () -> Int, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append interpolated pointer data to a log message.

 You don’t call this method directly. Instead, the framework calls it automatically when you append interpolated pointer data to a log message.

## Parameters

- `pointer`: The interpolated pointer data. The system automatically wraps this value in a closure.
- `bytes`: The size of the pointer in bytes.
- `format`: The format to apply to the value when the system renders it in a log message. For more information, see  . The default value is  .
- `privacy`: The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see  . The default value is  .
- `attributes`: Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see  .

## See Also

- [func appendInterpolation(@autoclosure () -> UnsafeRawPointer, bytes: @autoclosure () -> Int, format: OSLogPointerFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:bytes:format:privacy:).md)
  Appends interpolated pointer data.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-5qaau.md)
  Appends an interpolated collection of raw bytes.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs.md)
  Appends an interpolated collection of raw bytes with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:bytes:format:privacy:attributes:))*