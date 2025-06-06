# Message Argument Formatters

**Framework**: os

Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.

## Topics

### Privacy Options
- [struct OSLogPrivacy](oslogprivacy.md)
  The privacy options that determine when to redact or display values in log messages.
### Value Formatters
- [enum OSLogBoolFormat](oslogboolformat.md)
  The formatting options for Boolean values.
- [struct OSLogIntegerFormatting](oslogintegerformatting.md)
  The formatting options for integer values.
- [enum OSLogInt32ExtendedFormat](oslogint32extendedformat.md)
  The formatting options for 32-bit integer values.
- [struct OSLogFloatFormatting](oslogfloatformatting.md)
  The formatting options for double and floating-point numbers.
- [enum OSLogPointerFormat](oslogpointerformat.md)
  The formatting options for pointer data.
### Value Interpolation
- [struct OSLogInterpolation](osloginterpolation.md)
  A container for the elements of a log message.
- [enum OSLogIntExtendedFormat](oslogintextendedformat.md)
  Options for expanding bit rate information stored as an int during logging.
### String Alignment
- [struct OSLogStringAlignment](oslogstringalignment.md)
  The alignment options for interpolated strings.

## See Also

- [struct Logger](logger.md)
  An object for writing interpolated string messages to the unified logging system.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/message-argument-formatters)*