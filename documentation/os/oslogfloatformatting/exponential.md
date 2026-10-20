# exponential

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The standard exponential format option.

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
static var exponential: OSLogFloatFormatting { get }
```

## Mentions

- [Generating Log Messages from Your Code](../generating-log-messages-from-your-code.md)

#### Discussion

This option is equivalent to the `%e` option in `fprintf`. It prints the number in the form `[-]d.ddde±dd`, with `d` representing the digits of the number. The number of digits after the radix point is system-specific.

## See Also

### Getting the Standard Formats
- [static var fixed: OSLogFloatFormatting](./fixed.md)
  The standard fixed-point format option.
- [static var hex: OSLogFloatFormatting](./hex.md)
  The standard hexadecimal format for floating-point values.
- [static var hybrid: OSLogFloatFormatting](./hybrid.md)
  A hybrid option that changes the format according to the size of the number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogfloatformatting/exponential)*