# kAXContentsAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXContentsAttribute: String { get }
```

#### Discussion

Content-containing accessibility objects that are children of this accessibility object. For example, a tab view contains children that represent both the tab controls and the content displayed for each tab. The accessibility object representing a tab view can include only the content-display children in its `AXContents` attribute to help an assistive application provide more targeted information to the user. This attribute is recommended for any accessibility object whose children represent both content and control elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxcontentsattribute)*