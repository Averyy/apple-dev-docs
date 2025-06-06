# appendInterpolation(_:format:privacy:)

**Framework**: os  
**Kind**: method

Adds a Boolean argument to the message.

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
mutating func appendInterpolation(_ boolean: @autoclosure @escaping () -> Bool, format: OSLogBoolFormat = .truth, privacy: OSLogPrivacy = .auto)
```

#### Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## Parameters

- `boolean`: The Boolean value to add to the message.
- `format`: The format to apply to the Boolean value. You format Boolean values as either true/false or yes/no strings. If you don’t specify this parameter, the default format uses true/false strings. For more information, see  .
- `privacy`: The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-686xc)*