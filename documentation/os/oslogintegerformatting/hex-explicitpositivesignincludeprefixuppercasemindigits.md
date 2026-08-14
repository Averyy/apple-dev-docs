# hex(explicitPositiveSign:includePrefix:uppercase:minDigits:)

**Framework**: os  
**Kind**: method

Creates a custom hexidecimal format that includes a minimum number of digits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func hex(explicitPositiveSign: Bool = false, includePrefix: Bool = false, uppercase: Bool = false, minDigits: @autoclosure @escaping () -> Int) -> OSLogIntegerFormatting
```

#### Return Value

A custom hexadecimal format for integers.

## Parameters

- `explicitPositiveSign`: A Boolean value that indicates whether to display a plus (`+`) sign in front of positive integers.
- `includePrefix`: A Boolean value that indicates whether to include a `0x` prefix in front of the hexidecimal value.
- `uppercase`: A Boolean value that indicates whether to uppercase numerals that are greater than 9.
- `minDigits`: The minimum number of digits to display for the hexidecimal value. If the number of digits in the hexidecimal number is less than this value, the logging system adds leading zeros.

## See Also

- [static func decimal(explicitPositiveSign: Bool) -> OSLogIntegerFormatting](oslogintegerformatting/decimal(explicitpositivesign:).md)
  Creates a decimal format with custom handling of the numerical sign.
- [static func decimal(explicitPositiveSign: Bool, minDigits: @autoclosure () -> Int) -> OSLogIntegerFormatting](oslogintegerformatting/decimal(explicitpositivesign:mindigits:).md)
  Creates a decimal format with custom handling of the numerical sign and the minimum number of digits.
- [static func hex(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool) -> OSLogIntegerFormatting](oslogintegerformatting/hex(explicitpositivesign:includeprefix:uppercase:).md)
  Creates a custom hexidecimal format that displays the exact number of digits in the number.
- [static func octal(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool) -> OSLogIntegerFormatting](oslogintegerformatting/octal(explicitpositivesign:includeprefix:uppercase:).md)
  Creates a custom octal format that displays the exact number of digits in the number.
- [static func octal(explicitPositiveSign: Bool, includePrefix: Bool, uppercase: Bool, minDigits: @autoclosure () -> Int) -> OSLogIntegerFormatting](oslogintegerformatting/octal(explicitpositivesign:includeprefix:uppercase:mindigits:).md)
  Creates a custom octal format that includes a minimum number of digits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogintegerformatting/hex(explicitpositivesign:includeprefix:uppercase:mindigits:))*