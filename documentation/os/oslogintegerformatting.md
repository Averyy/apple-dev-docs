# OSLogIntegerFormatting

**Framework**: os  
**Kind**: struct

The formatting options for integer values.

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
struct OSLogIntegerFormatting
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Overview

An [`OSLogIntegerFormatting`](oslogintegerformatting.md) structure encapsulates the formatting details for integer numbers. Use the static [`decimal`](oslogintegerformatting/decimal.md), [`hex`](oslogintegerformatting/hex.md), and [`octal`](oslogintegerformatting/octal.md) structures to apply default formatting to integer values. You can also create new [`OSLogIntegerFormatting`](oslogintegerformatting.md) structures that customize the rules for handling a leading plus sign, special numerical prefixes, the minimum number of digits, and more.

## Topics

### Getting the Standard Formats
- [static var decimal: OSLogIntegerFormatting](oslogintegerformatting/decimal.md)
  The standard decimal format option.
- [static var hex: OSLogIntegerFormatting](oslogintegerformatting/hex.md)
  The standard hexadecimal format option.
- [static var octal: OSLogIntegerFormatting](oslogintegerformatting/octal.md)
  The standard octal format option.
### Creating a Custom Integer Format
- [static func decimal(explicitPositiveSign: Bool) -> OSLogIntegerFormatting](oslogintegerformatting/decimal(explicitpositivesign:).md)
  Creates a decimal format with custom handling of the numerical sign.
- [static func decimal(explicitPositiveSign: Bool, minDigits: @autoclosure () -> Int) -> OSLogIntegerFormatting](oslogintegerformatting/decimal(explicitpositivesign:mindigits:).md)
  Creates a decimal format with custom handling of the numerical sign and the minimum number of digits.
- [static func hex(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool) -> OSLogIntegerFormatting](oslogintegerformatting/hex(explicitpositivesign:includeprefix:uppercase:).md)
  Creates a custom hexidecimal format that displays the exact number of digits in the number.
- [static func hex(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool, minDigits: @autoclosure () -> Int) -> OSLogIntegerFormatting](oslogintegerformatting/hex(explicitpositivesign:includeprefix:uppercase:mindigits:).md)
  Creates a custom hexidecimal format that includes a minimum number of digits.
- [static func octal(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool) -> OSLogIntegerFormatting](oslogintegerformatting/octal(explicitpositivesign:includeprefix:uppercase:).md)
  Creates a custom octal format that displays the exact number of digits in the number.
- [static func octal(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool, minDigits: @autoclosure () -> Int) -> OSLogIntegerFormatting](oslogintegerformatting/octal(explicitpositivesign:includeprefix:uppercase:mindigits:).md)
  Creates a custom octal format that includes a minimum number of digits.

## See Also

- [enum OSLogBoolFormat](oslogboolformat.md)
  The formatting options for Boolean values.
- [enum OSLogInt32ExtendedFormat](oslogint32extendedformat.md)
  The formatting options for 32-bit integer values.
- [struct OSLogFloatFormatting](oslogfloatformatting.md)
  The formatting options for double and floating-point numbers.
- [enum OSLogPointerFormat](oslogpointerformat.md)
  The formatting options for pointer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogintegerformatting)*