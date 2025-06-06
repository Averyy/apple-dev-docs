# maxOSLogArgumentCount

**Framework**: os  
**Kind**: var

The maximum number of interpolated expressions that a log message may contain.

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
var maxOSLogArgumentCount: UInt8 { get }
```

#### Discussion

For log messages that include interpolated values, the system imposes a limit on the total number of expressions that a single message may include. The following example shows a string that contains an interpolated value:

```swift
let fileID = 941
let message = "Created a file with ID \(fileID)"
```

## See Also

- [var bufferSize: Int](oslogmessage/buffersize.md)
  The byte size of the buffer that the logging system receives.
- [let interpolation: OSLogInterpolation](oslogmessage/interpolation.md)
  The log message’s string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/maxoslogargumentcount)*