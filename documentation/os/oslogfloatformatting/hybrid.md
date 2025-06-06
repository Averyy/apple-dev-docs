# hybrid

**Framework**: os  
**Kind**: property

A hybrid option that changes the format according to the size of the number.

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
static var hybrid: OSLogFloatFormatting { get }
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Discussion

This option is equivalent to the `%g` option in `fprintf`. It behaves like the [`fixed`](oslogfloatformatting/fixed.md) option when the number is close to `1.0`, and like the [`exponential`](oslogfloatformatting/exponential.md) option when the number has a large exponent.

## See Also

- [static var fixed: OSLogFloatFormatting](oslogfloatformatting/fixed.md)
  The standard fixed-point format option.
- [static var hex: OSLogFloatFormatting](oslogfloatformatting/hex.md)
  The standard hexadecimal format for floating-point values.
- [static var exponential: OSLogFloatFormatting](oslogfloatformatting/exponential.md)
  The standard exponential format option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/hybrid)*