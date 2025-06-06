# left(columns:)

**Framework**: os  
**Kind**: method

Aligns the value on the left side of a column with the specified width.

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
static func left(columns: @autoclosure @escaping () -> Int) -> OSLogStringAlignment
```

#### Return Value

A string-alignment structure with the specified value.

## Parameters

- `columns`: The width of the item in characters.

## See Also

- [static func right(columns: @autoclosure () -> Int) -> OSLogStringAlignment](oslogstringalignment/right(columns:).md)
  Aligns the value on the right side of a column with the specified width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogstringalignment/left(columns:))*