# appendInterpolation(_:format:align:privacy:)

**Framework**: os  
**Kind**: method

Appends an interpolated integer.

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
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Int, format: OSLogIntegerFormatting = .decimal, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

#### Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## Parameters

- `number`: The integer value to add to the message.
- `format`: The format to apply to the integer value. You format integers as decimal, hexadecimal, or octal values. If you don’t specify this parameter, the default format uses a decimal value. For more information, see  .
- `align`: The alignment to apply to the value. Use this parameter to specify the width of the column containing the data, and the alignment of the data within that column. If you don’t specify this parameter, the system doesn’t align the value.
- `privacy`: The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## See Also

- [func appendInterpolation(@autoclosure () -> Int8, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-5ihzf.md)
  Appends an interpolated 8-bit integer.
- [func appendInterpolation(@autoclosure () -> Int16, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-190d0.md)
  Appends an interpolated 16-bit integer.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-3ji02.md)
  Appends an interpolated 32-bit integer.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir.md)
  Appends an interpolated 32-bit integer with the specified attributes.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-2sb1i.md)
  Appends an interpolated 32-bit integer with the specified alignment.
- [func appendInterpolation(@autoclosure () -> Int64, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-802m9.md)
  Appends an interpolated 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-8kli1)*