# appendInterpolation(_:bytes:format:privacy:)

**Framework**: os  
**Kind**: method

Appends interpolated pointer data.

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
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawPointer, bytes: @autoclosure @escaping () -> Int, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto)
```

#### Discussion

Don’t call this function directly. The system calls it automatically when interpolating values of this type. When specifying the value in your string, you may include any of the indicated parameters to change the default presentation of that value.

## Parameters

- `pointer`: The pointer with the contents you want to add to the message.
- `bytes`: The number of bytes in the pointer data.
- `format`: The format to apply to the pointer. You format pointers as one of several different options. If you don’t specify this parameter, the system doesn’t format the value. For more information, see  .
- `privacy`: The privacy level of the information. If you don’t specify this parameter, the system uses the default rules to determine whether to show the information.

## See Also

- [func appendInterpolation(@autoclosure () -> UnsafeRawPointer, bytes: @autoclosure () -> Int, format: OSLogPointerFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:bytes:format:privacy:attributes:).md)
  Appends interpolated pointer data with the specified attributes.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-5qaau.md)
  Appends an interpolated collection of raw bytes.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs.md)
  Appends an interpolated collection of raw bytes with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:bytes:format:privacy:))*