# exponential(precision:explicitPositiveSign:uppercase:)

**Framework**: os  
**Kind**: method

Creates a custom exponential format with the specified precision value.

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
static func exponential(precision: @autoclosure @escaping () -> Int, explicitPositiveSign: Bool = false, uppercase: Bool = false) -> OSLogFloatFormatting
```

#### Return Value

A custom exponential format for floating-point numbers.

## Parameters

- `precision`: The maximum number of digits to display to the right of the decimal point.
- `explicitPositiveSign`: A Boolean value that indicates whether to display a plus ( ) sign in front of positive numbers.
- `uppercase`: A Boolean value that indicates whether to uppercase letters that are part of the floating-point number. For example, it determines the capitalization of the exponent indicator   in the number  , or the letters in special values such as   and  .

## See Also

- [static func exponential(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/exponential(explicitpositivesign:uppercase:).md)
  Creates a custom exponential format with a system-determined precision value.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/exponential(precision:explicitpositivesign:uppercase:))*