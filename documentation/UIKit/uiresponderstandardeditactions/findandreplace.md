# findAndReplace(_:)

**Framework**: UIKit  
**Kind**: method

Begins a search for content in your app’s interface and provides a replacement.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func findAndReplace(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Find and Replace command from an editing menu. Your implementation should present the UI for finding and replacing textual content in your view.

For example, a view using a find interaction might call [`presentFindNavigator(showingReplace:)`](uifindinteraction/presentfindnavigator(showingreplace:).md) to present the system find panel.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func find(Any?)](uiresponderstandardeditactions/find(_:).md)
  Begins a search for content in your app’s interface.
- [func findNext(Any?)](uiresponderstandardeditactions/findnext(_:).md)
  Finds the next match in your app’s interface.
- [func findPrevious(Any?)](uiresponderstandardeditactions/findprevious(_:).md)
  Finds the previous match in your app’s interface.
- [func useSelectionForFind(Any?)](uiresponderstandardeditactions/useselectionforfind(_:).md)
  Begins a search for the selected content in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/findandreplace(_:))*