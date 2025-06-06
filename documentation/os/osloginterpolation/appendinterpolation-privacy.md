# appendInterpolation(_:privacy:)

**Framework**: os  
**Kind**: method

Appends an interpolated object description.

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
mutating func appendInterpolation(_ argumentObject: @autoclosure @escaping () -> NSObject, privacy: OSLogPrivacy = .auto)
```

#### Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## Parameters

- `argumentObject`: The object with the description you want to add to the message. This function calls the   method of the object and incorporates that value into the message string.
- `privacy`: The privacy level of the information. If you don’t specify this parameter, the default rules redact the object description.

## See Also

- [func appendInterpolation(@autoclosure () -> NSObject, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2.md)
  Appends an interpolated object description with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:privacy:))*