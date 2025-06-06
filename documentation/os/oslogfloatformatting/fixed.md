# fixed

**Framework**: os  
**Kind**: property

The standard fixed-point format option.

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
static var fixed: OSLogFloatFormatting { get }
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Discussion

This option is equivalent to the `%f` option of `fprintf`, which prints all digits before the radix point and a system-specific number of digits after the radix point.

## See Also

- [static var hex: OSLogFloatFormatting](oslogfloatformatting/hex.md)
  The standard hexadecimal format for floating-point values.
- [static var exponential: OSLogFloatFormatting](oslogfloatformatting/exponential.md)
  The standard exponential format option.
- [static var hybrid: OSLogFloatFormatting](oslogfloatformatting/hybrid.md)
  A hybrid option that changes the format according to the size of the number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/fixed)*