# kAXSharedCharacterRangeAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kAXSharedCharacterRangeAttribute: String { get }
```

#### Discussion

The portion of shared text this accessibility object currently displays. In a multi-column document, for example, each column may be represented by a separate accessibility object. However, the text in the document may flow from one column to the other. Get the value of this attribute if you need to know the specific range of characters this accessibility object currently displays. This attribute is recommended for sets of accessibility objects that share text in a single window. (See `kAXSharedTextUIElementsAttribute` for a related attribute.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxsharedcharacterrangeattribute)*