# kAXSelectedTextRangesAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.5+

## Declaration

```swift
var kAXSelectedTextRangesAttribute: String { get }
```

#### Discussion

An array of noncontiguous ranges of characters (not bytes) that defines the current selections of an editable text element.

Value: A CFArrayRef of kAXValueCFRanges.

Writable? Yes.

Recommended for text elements that support noncontiguous selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxselectedtextrangesattribute)*