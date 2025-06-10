# appendInterpolation(_:align:privacy:attributes:)

**Framework**: os  
**Kind**: method

Appends an interpolated string with the specified attributes.

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
mutating func appendInterpolation(_ argumentString: @autoclosure @escaping () -> String, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated string to a log message.

## Parameters

- `argumentString`: The interpolated string. The system automatically wraps this value in a closure.
- `align`: The alignment and minimum number of columns to use when the system renders the value in a log message. For more information, see  . The default value is  .
- `privacy`: The privacy level of the value, which the system applies when it renders the value in a log message. For more information, see  . The default value is  .
- `attributes`: Additional information about the value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any  e_ngineering types_ you embed in this value. For more information, see  .

## See Also

- [func appendInterpolation(@autoclosure () -> String, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-6tazr.md)
  Appends an interpolated string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-7g68v)*