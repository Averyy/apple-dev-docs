# shouldBeActive

**Framework**: Webkit  
**Kind**: property

Indicates whether the tab should be the active tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var shouldBeActive: Bool { get }
```

#### Discussion

If this property is `YES`, the tab should be made active in the window, ensuring it is the frontmost tab. Being active implies the tab is also selected. If this property is `NO`, the tab shouldn’t affect the currently active tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration/shouldbeactive)*