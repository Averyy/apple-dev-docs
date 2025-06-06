# kAXRoleDescriptionAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXRoleDescriptionAttribute: String { get }
```

#### Discussion

A localized string describing the role (for example, “button”). This string must be readable by (or speakable to) the user. All accessibility objects must include this attribute. To get the system-defined role description string for a given role, use the `HICopyAccessibilityRoleDescription` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxroledescriptionattribute)*