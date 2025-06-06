# kAXTopLevelUIElementAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kAXTopLevelUIElementAttribute: String { get }
```

#### Discussion

The window, sheet, or drawer element that contains this accessibility object. An accessibility object that is contained in a window, sheet, or drawer includes this attribute so an assistive application easily can find that element without having to step through all intervening objects in the accessibility hierarchy. This attribute is required for all accessibility objects whose parent or more distant ancestor represents a window, drawer, or sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxtopleveluielementattribute)*