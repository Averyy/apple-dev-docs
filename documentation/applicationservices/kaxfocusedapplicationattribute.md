# kAXFocusedApplicationAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXFocusedApplicationAttribute: String { get }
```

#### Discussion

Indicates the application element that is currently accepting keyboard input. This attribute is supported by the system-wide accessibility object to help an assistive application quickly determine the application that is accepting keyboard input. After the assistive application gets the accessibility object representing this application, it can send a message to the application asking for its focused accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxfocusedapplicationattribute)*