# hex(explicitPositiveSign:uppercase:)

**Framework**: os  
**Kind**: method

Creates a custom hexadecimal format.

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
static func hex(explicitPositiveSign: Bool = false, uppercase: Bool = false) -> OSLogFloatFormatting
```

#### Return Value

A custom hexadecimal format for floating-point numbers.

## Parameters

- `explicitPositiveSign`: A Boolean value that indicates whether to display a plus (`+`) sign in front of positive numbers.
- `uppercase`: A Boolean value that indicates whether to uppercase letters that are part of the floating-point number. In a hexidecimal number, it determines the capitalization of numerals above the number 9.

## See Also

- [static func exponential(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/exponential(explicitpositivesign:uppercase:).md)
  Creates a custom exponential format with a system-determined precision value.
- [static func exponential(precision: @autoclosure () -> Int, explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/exponential(precision:explicitpositivesign:uppercase:).md)
  Creates a custom exponential format with the specified precision value.
- [static func fixed(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/fixed(explicitpositivesign:uppercase:).md)
  Creates a custom fixed-point format with a system-determined precision value.
- [static func fixed(precision: @autoclosure () -> Int, explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/fixed(precision:explicitpositivesign:uppercase:).md)
  Creates a custom fixed-point format with the specified precision value.
- [static func hybrid(explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/hybrid(explicitpositivesign:uppercase:).md)
  Creates a custom hybrid format with a system-determined precision value.
- [static func hybrid(precision: @autoclosure () -> Int, explicitPositiveSign: Bool, uppercase: Bool) -> OSLogFloatFormatting](oslogfloatformatting/hybrid(precision:explicitpositivesign:uppercase:).md)
  Creates a custom hybrid format with the precision value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/hex(explicitpositivesign:uppercase:))*