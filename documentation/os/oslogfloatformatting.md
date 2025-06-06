# OSLogFloatFormatting

**Framework**: os  
**Kind**: struct

The formatting options for double and floating-point numbers.

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
struct OSLogFloatFormatting
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Overview

An [`OSLogFloatFormatting`](oslogfloatformatting.md) structure encapsulates the formatting details for `double` and `float` values. Use the static [`fixed`](oslogfloatformatting/fixed.md), [`hex`](oslogfloatformatting/hex.md), [`exponential`](oslogfloatformatting/exponential.md), and [`hybrid`](oslogfloatformatting/hybrid.md) structures to apply default formatting for floating-point values. You can also create new [`OSLogFloatFormatting`](oslogfloatformatting.md) structures that customize the rules for handling a leading plus sign, precision information, and more.

## Topics

### Getting the Standard Formats
- [static var fixed: OSLogFloatFormatting](oslogfloatformatting/fixed.md)
  The standard fixed-point format option.
- [static var hex: OSLogFloatFormatting](oslogfloatformatting/hex.md)
  The standard hexadecimal format for floating-point values.
- [static var exponential: OSLogFloatFormatting](oslogfloatformatting/exponential.md)
  The standard exponential format option.
- [static var hybrid: OSLogFloatFormatting](oslogfloatformatting/hybrid.md)
  A hybrid option that changes the format according to the size of the number.
### Creating a Custom Formatting Object
- [static func exponential(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/exponential(explicitpositivesign:uppercase:).md)
  Creates a custom exponential format with a system-determined precision value.
- [static func exponential(precision: @autoclosure () -> Int, explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/exponential(precision:explicitpositivesign:uppercase:).md)
  Creates a custom exponential format with the specified precision value.
- [static func fixed(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/fixed(explicitpositivesign:uppercase:).md)
  Creates a custom fixed-point format with a system-determined precision value.
- [static func fixed(precision: @autoclosure () -> Int, explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/fixed(precision:explicitpositivesign:uppercase:).md)
  Creates a custom fixed-point format with the specified precision value.
- [static func hex(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/hex(explicitpositivesign:uppercase:).md)
  Creates a custom hexadecimal format.
- [static func hybrid(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/hybrid(explicitpositivesign:uppercase:).md)
  Creates a custom hybrid format with a system-determined precision value.
- [static func hybrid(precision: @autoclosure () -> Int, explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/hybrid(precision:explicitpositivesign:uppercase:).md)
  Creates a custom hybrid format with the precision value.

## See Also

- [enum OSLogBoolFormat](oslogboolformat.md)
  The formatting options for Boolean values.
- [struct OSLogIntegerFormatting](oslogintegerformatting.md)
  The formatting options for integer values.
- [enum OSLogInt32ExtendedFormat](oslogint32extendedformat.md)
  The formatting options for 32-bit integer values.
- [enum OSLogPointerFormat](oslogpointerformat.md)
  The formatting options for pointer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting)*