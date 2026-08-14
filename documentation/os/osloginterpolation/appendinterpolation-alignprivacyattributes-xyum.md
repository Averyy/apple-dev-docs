# appendInterpolation(_:align:privacy:attributes:)

**Framework**: os  
**Kind**: method

Appends an interpolated textual representation of a type using the specified attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
mutating func appendInterpolation<T>(_ value: @autoclosure @escaping () -> T, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String) where T : CustomStringConvertible
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated type that adopts the [`CustomStringConvertible`](https://developer.apple.com/documentation/swift/customstringconvertible) protocol to a log message.

## Parameters

- `value`: The interpolated type, which the system automatically wraps in a closure. The type itself doesn’t appear in the log message. Instead, the system incorporates the textual representation the type provides through its implementation of the [`CustomStringConvertible`](https://developer.apple.com/documentation/swift/customstringconvertible) protocol.
- `align`: The alignment and minimum number of columns to use when the system renders the value in a log message. For more information, see [`OSLogStringAlignment`](oslogstringalignment.md). The default value is [`none`](oslogstringalignment/none.md).
- `privacy`: The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [`OSLogPrivacy`](oslogprivacy.md). The default value is [`auto`](oslogprivacy/auto.md).
- `attributes`: Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [`Instruments Developer Help`](https://developer.apple.comhttps://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## See Also

- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-84m60.md)
  Appends an interpolated textual representation of a type.
- [func appendInterpolation<T>(@autoclosure () -> T, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8107a.md)
  Appends an interpolated numeric type using the specified attributes.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt.md)
  Appends an interpolated type description.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-9hehv.md)
  Appends an interpolated type description with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-xyum)*