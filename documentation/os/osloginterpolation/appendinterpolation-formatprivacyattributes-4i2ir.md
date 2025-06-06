# appendInterpolation(_:format:privacy:attributes:)

**Framework**: os  
**Kind**: method

Appends an interpolated 32-bit integer with the specified attributes.

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
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy = .auto, attributes: String)
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated 32-bit integer to a log message.

 You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated 32-bit integer to a log message.

## Parameters

- `number`: The interpolated 32-bit integer. The system automatically wraps this value in a closure.
- `format`: The format to apply to the value when the system renders it in a log message. For more information, see  .
- `privacy`: The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see  . The default value is  .
- `attributes`: Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see  .

## See Also

- [func appendInterpolation(@autoclosure () -> Int, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-8kli1.md)
  Appends an interpolated integer.
- [func appendInterpolation(@autoclosure () -> Int8, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-5ihzf.md)
  Appends an interpolated 8-bit integer.
- [func appendInterpolation(@autoclosure () -> Int16, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-190d0.md)
  Appends an interpolated 16-bit integer.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-3ji02.md)
  Appends an interpolated 32-bit integer.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-2sb1i.md)
  Appends an interpolated 32-bit integer with the specified alignment.
- [func appendInterpolation(@autoclosure () -> Int64, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-802m9.md)
  Appends an interpolated 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir)*