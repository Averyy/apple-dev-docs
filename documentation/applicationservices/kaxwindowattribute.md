# kAXWindowAttribute

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXWindowAttribute: String { get }
```

#### Discussion

The window element that contains this accessibility object. An accessibility object that is contained in a window includes this attribute so an assistive application easily can find the window without having to step through all intervening objects in the accessibility hierarchy. Note that the value of the `AXWindow` attribute must be an accessibility object that represents a window, not a sheet or drawer. For a similar attribute that is less restrictive, see `kAXTopLevelUIElementAttribute`. The `AXWindow` attribute is required for all accessibility elements whose parent or more distant ancestor represents a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxwindowattribute)*