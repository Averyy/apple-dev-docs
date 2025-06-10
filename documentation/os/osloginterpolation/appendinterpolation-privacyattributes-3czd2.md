# appendInterpolation(_:privacy:attributes:)

**Framework**: os  
**Kind**: method

Appends an interpolated object description with the specified attributes.

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
mutating func appendInterpolation(_ argumentObject: @autoclosure @escaping () -> NSObject, privacy: OSLogPrivacy = .auto, attributes: String)
```

#### Discussion

> ❗ **Important**:  You don’t call this method directly. Instead, the framework calls it automatically when you append an interpolated object description to a log message.

## Parameters

- `argumentObject`: The interpolated object, which the system automatically wraps in a closure. The object itself doesn’t appear in the log message. Instead, the system calls the object’s   method and incorporates the value it returns.
- `privacy`: The privacy level of the interpolated value, which the system applies when it renders the value in a log message. For more information, see  . The default value is  .
- `attributes`: Additional information about the interpolated value. Tools that process log messages interpret these attributes, which you typically provide as key-value pairs. For example, Instruments processes any e_ngineering types_ you embed in this value. For more information, see  .

## See Also

- [func appendInterpolation(@autoclosure () -> NSObject, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:privacy:).md)
  Appends an interpolated object description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2)*