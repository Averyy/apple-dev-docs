# lines

**Framework**: XcodeKit  
**Kind**: property

The lines of text in the buffer, including line endings.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var lines: NSMutableArray { get }
```

#### Discussion

Line breaks within a single buffer should be consistent. Adding a line containing additional line breaks modifies the array such that each line added is a separate element. Changes to the `completeBuffer` property are immediately reflected in this property, and vice versa.

## See Also

- [var selections: NSMutableArray](xcsourcetextbuffer/selections.md)
  The text selections in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextbuffer/lines)*