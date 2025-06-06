# appendInterpolation(_:align:privacy:)

**Framework**: os  
**Kind**: method

Appends an interpolated type description.

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
mutating func appendInterpolation(_ value: @autoclosure @escaping () -> any Any.Type, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

#### Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## Parameters

- `value`: A Swift type.
- `align`: The alignment to apply to the type name. Use this parameter to specify the width of the column containing the name, and the alignment of the name within that column. If you don’t specify this parameter, the system doesn’t align the value.
- `privacy`: The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## See Also

- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-84m60.md)
  Appends an interpolated textual representation of a type.
- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-xyum.md)
  Appends an interpolated textual representation of a type using the specified attributes.
- [func appendInterpolation<T>(@autoclosure () -> T, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8107a.md)
  Appends an interpolated numeric type using the specified attributes.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-9hehv.md)
  Appends an interpolated type description with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt)*