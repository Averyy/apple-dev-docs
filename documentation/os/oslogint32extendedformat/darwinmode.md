# OSLogInt32ExtendedFormat.darwinMode

**Framework**: os  
**Kind**: case

A format that displays a 32-bit integer as a Darwin file mode.

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
case darwinMode
```

#### Discussion

Use this option to format the interpolated value as a Darwin file mode, such as `-rwx------`. Because Darwin uses octal values to represent file modes numerically, pass an octal literal to the formatter. Alternatively, convert the octal value to its 32-bit integer equivalent and interpolate that instead. For more information about using octal literals, see [`Numeric Literals`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID323).

The following example formats the octal literal `0o700` using the `darwinMode` formatter:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
        
// Darwin uses octal values to represent file modes. Use Swift's
// support for octal literals to assign a file mode to a 32-bit 
// integer variable.
let value: Int32 = 0o700
        
// Write the value to the log using the specified format.
logger.info(".darwinMode output is \(value, format: .darwinMode)")
```

And the system writes the following message to the log:

```None
[Formatter Output] .darwinMode formats the value as -rwx------
```

## See Also

- [OSLogInt32ExtendedFormat.ipv4Address](oslogint32extendedformat/ipv4address.md)
  A format that displays a 32-bit integer as an IPv4 address.
- [OSLogInt32ExtendedFormat.secondsSince1970](oslogint32extendedformat/secondssince1970.md)
  A format that displays a 32-bit integer as a date.
- [OSLogInt32ExtendedFormat.darwinErrno](oslogint32extendedformat/darwinerrno.md)
  A format that displays a 32-bit integer as a Darwin error number.
- [OSLogInt32ExtendedFormat.darwinSignal](oslogint32extendedformat/darwinsignal.md)
  A format that displays a 32-bit integer as a Darwin signal.
- [OSLogInt32ExtendedFormat.bitrate](oslogint32extendedformat/bitrate.md)
  A format that displays a 32-bit integer as a bit rate.
- [OSLogInt32ExtendedFormat.bitrateIEC](oslogint32extendedformat/bitrateiec.md)
  A format that displays a 32-bit integer as an IEC bit rate.
- [OSLogInt32ExtendedFormat.byteCount](oslogint32extendedformat/bytecount.md)
  A format that displays a 32-bit integer as bytes.
- [OSLogInt32ExtendedFormat.byteCountIEC](oslogint32extendedformat/bytecountiec.md)
  A format that displays a 32-bit integer as IEC bytes.
- [OSLogInt32ExtendedFormat.truth](oslogint32extendedformat/truth.md)
  A format that displays a 32-bit integer as true or false.
- [OSLogInt32ExtendedFormat.answer](oslogint32extendedformat/answer.md)
  A format that displays a 32-bit integer as yes or no.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogint32extendedformat/darwinmode)*