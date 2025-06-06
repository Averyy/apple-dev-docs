# decimal(explicitPositiveSign:)

**Framework**: os  
**Kind**: method

Creates a decimal format with custom handling of the numerical sign.

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
static func decimal(explicitPositiveSign: Bool = false) -> OSLogIntegerFormatting
```

#### Return Value

A custom decimal format for integers.

## Parameters

- `explicitPositiveSign`: A Boolean value that indicates whether to display a plus ( ) sign in front of positive integers.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogintegerformatting/decimal(explicitpositivesign:))*