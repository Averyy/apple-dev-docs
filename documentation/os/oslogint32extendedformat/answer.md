# OSLogInt32ExtendedFormat.answer

**Framework**: os  
**Kind**: case  
**Role**: Case

A format that displays a 32-bit integer as yes or no.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
case answer
```

## Discussion

Use this option to format the interpolated value as either `YES` or `NO`. The formatter converts all positive and negative nonzero values to `YES`, and only zero to `NO`. The following example applies the answer formatter to the 32-bit integer value `0`:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate.
let value: Int32 = 0
                
// Write the value to the log using the specified format.
logger.info(".answer output is \(value, format: .answer)")
```

And the system writes the following message to the log:

```
[Formatter Output] .answer output is NO
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
- [OSLogInt32ExtendedFormat.byteCountIEC](./bytecountiec.md)
  A format that displays a 32-bit integer as IEC bytes.
- [OSLogInt32ExtendedFormat.truth](./truth.md)
  A format that displays a 32-bit integer as true or false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogint32extendedformat/answer)*