# OSLogInt32ExtendedFormat.ipv4Address

**Framework**: os  
**Kind**: case

A format that displays a 32-bit integer as an IPv4 address.

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
case ipv4Address
```

#### Discussion

Use this option to format the interpolated value as an IPv4 address, such as `127.0.0.1`. The following example applies the `ipv4Address` formatter to the 32-bit integer value `0x0100007f`:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate.
let value: Int32 = 0x0100007f
                
// Write the value to the log using the specified format.
logger.info(".ipv4Address output is \(value, format: .ipv4Address)")
```

And the system writes the following message to the log:

```None
[Formatter Output] .ipv4Address output is 127.0.0.1
```

## See Also

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
- [OSLogInt32ExtendedFormat.truth](oslogint32extendedformat/truth.md)
  A format that displays a 32-bit integer as true or false.
- [OSLogInt32ExtendedFormat.answer](oslogint32extendedformat/answer.md)
  A format that displays a 32-bit integer as yes or no.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogint32extendedformat/ipv4address)*