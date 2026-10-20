# hybrid

**Framework**: os  
**Kind**: property  
**Role**: Type Property

A hybrid option that changes the format according to the size of the number.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
static var hybrid: OSLogFloatFormatting { get }
```

## Mentions

- [Generating Log Messages from Your Code](../generating-log-messages-from-your-code.md)

#### Discussion

This option is equivalent to the `%g` option in `fprintf`. It behaves like the [`fixed`](./fixed.md) option when the number is close to `1.0`, and like the [`exponential`](./exponential.md) option when the number has a large exponent.

## See Also

### Getting the Standard Formats
- [static var fixed: OSLogFloatFormatting](./fixed.md)
  The standard fixed-point format option.
- [static var hex: OSLogFloatFormatting](./hex.md)
  The standard hexadecimal format for floating-point values.
- [static var exponential: OSLogFloatFormatting](./exponential.md)
  The standard exponential format option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/hybrid)*