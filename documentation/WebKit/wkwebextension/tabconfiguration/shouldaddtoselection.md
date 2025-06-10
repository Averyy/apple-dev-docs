# shouldAddToSelection

**Framework**: WebKit  
**Kind**: property

Indicates whether the tab should be added to the current tab selection.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var shouldAddToSelection: Bool { get }
```

#### Discussion

If this property is `YES`, the tab should be part of the current selection, but not necessarily become the active tab unless [`shouldBeActive`](wkwebextension/tabconfiguration/shouldbeactive.md) is also `YES`. If this property is `NO`, the tab shouldn’t be part of the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration/shouldaddtoselection)*