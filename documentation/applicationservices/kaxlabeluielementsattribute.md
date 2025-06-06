# kAXLabelUIElementsAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kAXLabelUIElementsAttribute: String { get }
```

#### Discussion

An array of accessibility objects representing the labels displayed near the control represented by this accessibility object. For example, a slider control might display labels that indicate the range of values the slider can represent. Because these labels are not displayed as part of the slider’s visual interface, an assistive application does not know they are associated with the slider. By including accessibility objects representing the labels in this attribute, you make this association explicit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxlabeluielementsattribute)*