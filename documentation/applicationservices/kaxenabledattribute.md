# kAXEnabledAttribute

**Framework**: Application Services  
**Kind**: data  
**Role**: Global Variable

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXEnabledAttribute: String { get }
```

```c
#define kAXEnabledAttribute
```

## Discussion

Indicates whether the user can interact with the accessibility object. For example, the `AXEnabled` attribute of a disabled button is `false`. This attribute is required for accessibility objects that represent views, menus, and menu items. This attribute is not required for accessibility objects that represent windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxenabledattribute)*