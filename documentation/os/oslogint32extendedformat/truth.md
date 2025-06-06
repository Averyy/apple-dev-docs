# OSLogInt32ExtendedFormat.truth

**Framework**: os  
**Kind**: case

A format that displays a 32-bit integer as true or false.

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
case truth
```

#### Discussion

Use this option to format the interpolated value as either `true` or `false`. The formatter converts all positive and negative nonzero values to `true`, and only zero to `false`. The following example applies the `truth` formatter to the 32-bit integer value `0`:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate.
let value: Int32 = 0
                
// Write the value to the log using the specified format.
logger.info(".truth output is \(value, format: .truth)")
```

And the system writes the following message to the log:

```None
[Formatter Output] .truth output is false
```

## See Also

- [OSLogInt32ExtendedFormat.ipv4Address](oslogint32extendedformat/ipv4address.md)
  A format that displays a 32-bit integer as an IPv4 address.
- [OSLogInt32ExtendedFormat.secondsSince1970](oslogint32extendedformat/secondssince1970.md)
  A format that displays a 32-bit integer as a date.
- [OSLogInt32ExtendedFormat.darwinErrno](oslogint32extendedformat/darwinerrno.md)
  A format that displays a 32-bit integer as a Darwin error number.
- [OSLogInt32ExtendedFormat.darwinMode](oslogint32extendedformat/darwinmode.md)
  A format that displays a 32-bit integer as a Darwin file mode.
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
- [OSLogInt32ExtendedFormat.answer](oslogint32extendedformat/answer.md)
  A format that displays a 32-bit integer as yes or no.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogint32extendedformat/truth)*