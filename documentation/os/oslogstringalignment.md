# OSLogStringAlignment

**Framework**: os  
**Kind**: struct

The alignment options for interpolated strings.

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
struct OSLogStringAlignment
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

## Topics

### Getting the Standard Alignment
- [static var none: OSLogStringAlignment](oslogstringalignment/none.md)
  No alignment.
### Getting a Custom String Alignment
- [static func left(columns: @autoclosure () -> Int) -> OSLogStringAlignment](oslogstringalignment/left(columns:).md)
  Aligns the value on the left side of a column with the specified width.
- [static func right(columns: @autoclosure () -> Int) -> OSLogStringAlignment](oslogstringalignment/right(columns:).md)
  Aligns the value on the right side of a column with the specified width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogstringalignment)*