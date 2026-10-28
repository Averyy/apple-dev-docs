# fixed

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The standard fixed-point format option.

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
static var fixed: OSLogFloatFormatting { get }
```

## Mentions

- [Generating Log Messages from Your Code](../generating-log-messages-from-your-code.md)

## Discussion

This option is equivalent to the `%f` option of `fprintf`, which prints all digits before the radix point and a system-specific number of digits after the radix point.

## See Also

### Getting the Standard Formats
- [static var hex: OSLogFloatFormatting](./hex.md)
  The standard hexadecimal format for floating-point values.
- [static var exponential: OSLogFloatFormatting](./exponential.md)
  The standard exponential format option.
- [static var hybrid: OSLogFloatFormatting](./hybrid.md)
  A hybrid option that changes the format according to the size of the number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/fixed)*