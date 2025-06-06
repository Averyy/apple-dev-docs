# OSLogInterpolation

**Framework**: os  
**Kind**: struct

A container for the elements of a log message.

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
@frozen
struct OSLogInterpolation
```

#### Overview

An [`OSLogInterpolation`](osloginterpolation.md) structure contains a formatted string and its interpolated arguments. Don’t create [`OSLogInterpolation`](osloginterpolation.md) structures directly. The system creates them automatically when you log messages using the [`Logger`](logger.md) object.

When you craft log messages, you may incorporate content from your code’s variables directly into the message strings. When you do, the logging system creates [`OSLogInterpolation`](osloginterpolation.md) structures to store those values. The structure stores the provided values as-is, and the logging system formats those values as strings only in the final log message. To change the final appearance of a value, include additional parameters along with the value. Consider the following example, which logs values of several different types:

```swift
logger.log("\(taskID) \(giftCardID) \(serverID) \(seconds)")
```

For values that are variable in length, formatting them makes the log message easier to read. In the preceding example, `giftCardID` and `seconds` contain variable-length values. The following example fixes the formatting issues by making all gift card IDs the same width and aligning them to the left edge of the available space. The example also formats each seconds value as a fixed-point number with only two digits to the right of the decimal point.

```swift
logger.log("\(taskID) \(giftCardID, align: .left(columns: GiftCard.maxIDLength)) \(serverID) \(seconds, format: .fixed(precision: 2))")
```

Because strings and custom objects may contain user-sensitive information, the logging system redacts those values by default, however, it doesn’t redact numerical values. The resulting log message displays a string like `<private>` instead of the actual value. If you know the value doesn’t include sensitive data, change the privacy setting using the `privacy` parameter, as the following example shows:

```swift
logger.log("Paid with bank account \(accountNumberString)")   // Redacted by default
logger.log("Ordered smoothie \(smoothieName, privacy: .public)")  // Visible!
```

## Topics

### Appending Strings
- [func appendInterpolation(@autoclosure () -> String, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-6tazr.md)
  Appends an interpolated string.
- [func appendInterpolation(@autoclosure () -> String, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-7g68v.md)
  Appends an interpolated string with the specified attributes.
### Appending Signed Integers
- [func appendInterpolation(@autoclosure () -> Int, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-8kli1.md)
  Appends an interpolated integer.
- [func appendInterpolation(@autoclosure () -> Int8, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-5ihzf.md)
  Appends an interpolated 8-bit integer.
- [func appendInterpolation(@autoclosure () -> Int16, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-190d0.md)
  Appends an interpolated 16-bit integer.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-3ji02.md)
  Appends an interpolated 32-bit integer.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir.md)
  Appends an interpolated 32-bit integer with the specified attributes.
- [func appendInterpolation(@autoclosure () -> Int32, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-2sb1i.md)
  Appends an interpolated 32-bit integer with the specified alignment.
- [func appendInterpolation(@autoclosure () -> Int64, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-802m9.md)
  Appends an interpolated 64-bit integer.
### Appending Unsigned Integers
- [func appendInterpolation(@autoclosure () -> UInt, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-20jin.md)
  Appends an interpolated unsigned integer.
- [func appendInterpolation(@autoclosure () -> UInt8, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-4qvu9.md)
  Appends an interpolated unsigned 8-bit integer.
- [func appendInterpolation(@autoclosure () -> UInt16, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-7k91g.md)
  Appends an interpolated unsigned 16-bit integer.
- [func appendInterpolation(@autoclosure () -> UInt32, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-2i3qh.md)
  Appends an interpolated unsigned 32-bit integer.
- [func appendInterpolation(@autoclosure () -> UInt64, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-81jbm.md)
  Appends an interpolated unsigned 64-bit integer.
### Appending Doubles
- [func appendInterpolation(@autoclosure () -> Double, format: OSLogFloatFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-6mu00.md)
  Appends an interpolated double.
- [func appendInterpolation(@autoclosure () -> Double, format: OSLogFloatFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8bi90.md)
  Appends an interpolated double with the specified attributes.
### Appending Floats
- [func appendInterpolation(@autoclosure () -> Float, format: OSLogFloatFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:align:privacy:)-7z1jd.md)
  Appends an interpolated float.
- [func appendInterpolation(@autoclosure () -> Float, format: OSLogFloatFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-78sek.md)
  Appends an interpolated float with the specified attributes.
### Appending Boolean Values
- [func appendInterpolation(@autoclosure () -> Bool, format: OSLogBoolFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-686xc.md)
  Adds a Boolean argument to the message.
### Appending Generic Types
- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-84m60.md)
  Appends an interpolated textual representation of a type.
- [func appendInterpolation<T>(@autoclosure () -> T, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-xyum.md)
  Appends an interpolated textual representation of a type using the specified attributes.
- [func appendInterpolation<T>(@autoclosure () -> T, format: OSLogIntegerFormatting, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:align:privacy:attributes:)-8107a.md)
  Appends an interpolated numeric type using the specified attributes.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt.md)
  Appends an interpolated type description.
- [func appendInterpolation(@autoclosure () -> any Any.Type, align: OSLogStringAlignment, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-9hehv.md)
  Appends an interpolated type description with the specified attributes.
### Appending Pointer Data
- [func appendInterpolation(@autoclosure () -> UnsafeRawPointer, bytes: @autoclosure () -> Int, format: OSLogPointerFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:bytes:format:privacy:).md)
  Appends interpolated pointer data.
- [func appendInterpolation(@autoclosure () -> UnsafeRawPointer, bytes: @autoclosure () -> Int, format: OSLogPointerFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:bytes:format:privacy:attributes:).md)
  Appends interpolated pointer data with the specified attributes.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:format:privacy:)-5qaau.md)
  Appends an interpolated collection of raw bytes.
- [func appendInterpolation(@autoclosure () -> UnsafeRawBufferPointer, format: OSLogPointerFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs.md)
  Appends an interpolated collection of raw bytes with the specified attributes.
### Appending Objects
- [func appendInterpolation(@autoclosure () -> NSObject, privacy: OSLogPrivacy)](osloginterpolation/appendinterpolation(_:privacy:).md)
  Appends an interpolated object description.
- [func appendInterpolation(@autoclosure () -> NSObject, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2.md)
  Appends an interpolated object description with the specified attributes.
### Instance Methods
- [func appendInterpolation(@autoclosure () -> Int, format: OSLogIntExtendedFormat, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-6le5w.md)
- [func appendInterpolation(@autoclosure () -> any Error, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:privacy:attributes:)-4o74h.md)
- [func appendInterpolation(@autoclosure () -> (any Error)?, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:privacy:attributes:)-6vtcc.md)
- [func appendInterpolation(@autoclosure () -> NSObject?, privacy: OSLogPrivacy, attributes: String)](osloginterpolation/appendinterpolation(_:privacy:attributes:)-9eafm.md)

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)

## See Also

- [enum OSLogIntExtendedFormat](oslogintextendedformat.md)
  Options for expanding bit rate information stored as an int during logging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osloginterpolation)*