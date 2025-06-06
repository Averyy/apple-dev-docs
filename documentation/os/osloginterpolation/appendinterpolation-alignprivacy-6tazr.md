# appendInterpolation(_:align:privacy:)

**Framework**: os  
**Kind**: method

Appends an interpolated string.

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
mutating func appendInterpolation(_ argumentString: @autoclosure @escaping () -> String, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

#### Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## Parameters

- `argumentString`: The interpolated string value to add to the message.
- `align`: The alignment to apply to the string. Use this parameter to specify the width of the column that contains the data, and the alignment of the data within that column. If you don’t specify this parameter, the system doesn’t align the value.
- `privacy`: The privacy level of the information. If you don’t specify this parameter, the default rules redact the string’s value.

## See Also

- [func appendInterpolation(@autoclosure () -> String, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-7g68v.md)
  Appends an interpolated string with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-6tazr)*