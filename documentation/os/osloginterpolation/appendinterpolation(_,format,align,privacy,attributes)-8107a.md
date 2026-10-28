# appendInterpolation(_:format:align:privacy:attributes:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Appends an interpolated numeric type using the specified attributes.

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
mutating func appendInterpolation<T>(_ number: @autoclosure @escaping () -> T, format: OSLogIntegerFormatting = .decimal, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String) where T : FixedWidthInteger
```

## Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated type that adopts the [`FixedWidthInteger`](../../Swift/fixedwidthinteger.md) protocol to a log message.

## Parameters

- `number`: The interpolated numeric type, which the system automatically wraps in a closure. The type itself doesn’t appear in the log message. Instead, the system incorporates the type’s integer value.
- `format`: The format to apply to the value when the system renders it in a log message. For more information, see [`OSLogIntegerFormatting`](../oslogintegerformatting.md). The default value is [`decimal`](../oslogintegerformatting/decimal.md).
- `align`: The alignment and minimum number of columns to use when the system renders the value in a log message. For more information, see [`OSLogStringAlignment`](../oslogstringalignment.md). The default value is [`none`](../oslogstringalignment/none.md).
- `privacy`: The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see [`OSLogPrivacy`](../oslogprivacy.md). The default value is [`auto`](../oslogprivacy/auto.md).
- `attributes`: Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31).

## See Also

### Appending Generic Types
- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy)](./appendinterpolation%28_,align,privacy%29-84m60.md)
  Appends an interpolated textual representation of a type.
- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](./appendinterpolation%28_,align,privacy,attributes%29-xyum.md)
  Appends an interpolated textual representation of a type using the specified attributes.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy)](./appendinterpolation%28_,align,privacy%29-8hwmt.md)
  Appends an interpolated type description.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](./appendinterpolation%28_,align,privacy,attributes%29-9hehv.md)
  Appends an interpolated type description with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8107a)*