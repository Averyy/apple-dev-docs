# kAXOrientationAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXOrientationAttribute: String { get }
```

#### Discussion

Indicates whether this accessibility object is displayed or interacted with in a vertical or a horizontal manner. The interpretation of an element, such as a slider, can change depending on whether it is oriented vertically or horizontally. Using the value of this attribute, an assistive application can communicate this information to the user. This attribute is required for any accessibility object, such as a scroller or slider, whose semantic meaning varies with the object’s orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxorientationattribute)*