# OSLogInt32ExtendedFormat.byteCountIEC

**Framework**: os  
**Kind**: case  
**Role**: Case

A format that displays a 32-bit integer as IEC bytes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
case byteCountIEC
```

## Discussion

Use this option to format the interpolated value as IEC bytes, such as `100 KiB`. The following example applies the `byteCountIEC` formatter to the 32-bit integer value `102_400`:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate.
let value: Int32 = 102_400
                
// Write the value to the log using the specified format.
logger.info(".byteCountIEC output is \(value, format: .byteCountIEC)")
```

And the system writes the following message to the log:

```
[Formatter Output] .byteCountIEC output is 100 KiB
```

## See Also

### Getting the Formats
- [OSLogInt32ExtendedFormat.ipv4Address](./ipv4address.md)
  A format that displays a 32-bit integer as an IPv4 address.
- [OSLogInt32ExtendedFormat.secondsSince1970](./secondssince1970.md)
  A format that displays a 32-bit integer as a date.
- [OSLogInt32ExtendedFormat.darwinErrno](./darwinerrno.md)
  A format that displays a 32-bit integer as a Darwin error number.
- [OSLogInt32ExtendedFormat.darwinMode](./darwinmode.md)
  A format that displays a 32-bit integer as a Darwin file mode.
- [OSLogInt32ExtendedFormat.darwinSignal](./darwinsignal.md)
  A format that displays a 32-bit integer as a Darwin signal.
- [OSLogInt32ExtendedFormat.bitrate](./bitrate.md)
  A format that displays a 32-bit integer as a bit rate.
- [OSLogInt32ExtendedFormat.bitrateIEC](./bitrateiec.md)
  A format that displays a 32-bit integer as an IEC bit rate.
- [OSLogInt32ExtendedFormat.byteCount](./bytecount.md)
  A format that displays a 32-bit integer as bytes.
- [OSLogInt32ExtendedFormat.truth](./truth.md)
  A format that displays a 32-bit integer as true or false.
- [OSLogInt32ExtendedFormat.answer](./answer.md)
  A format that displays a 32-bit integer as yes or no.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogint32extendedformat/bytecountiec)*