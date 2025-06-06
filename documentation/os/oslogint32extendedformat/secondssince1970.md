# OSLogInt32ExtendedFormat.secondsSince1970

**Framework**: os  
**Kind**: case

A format that displays a 32-bit integer as a date.

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
case secondsSince1970
```

#### Discussion

Use this option to format the interpolated value as a date and time, such as `2007-01-09 09:41:00`. The formatter considers the value you provide as a duration, in seconds, and adds it to the UNIX epoch to calculate the date it displays. The UNIX epoch is a method of describing a specific point in time using the elapsed number of seconds since 00:00:00 UTC January 1, 1970.

The following example applies the `secondsSince1970` formatter to the 32-bit integer value `604_800`, which is the exact number of seconds in one week:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate. In this case, the number of
// seconds in an entire week.
let value: Int32 = 604_800
                
// Write the value to the log using the specified format.
logger.info(".secondsSince1970 output is \(value, format: .secondsSince1970)")
```

And the system writes the following message to the log:

```None
[Formatter Output] .secondsSince1970 output is 1970-01-08 00:00:00
```

## See Also

- [OSLogInt32ExtendedFormat.ipv4Address](oslogint32extendedformat/ipv4address.md)
  A format that displays a 32-bit integer as an IPv4 address.
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

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogint32extendedformat/secondssince1970)*