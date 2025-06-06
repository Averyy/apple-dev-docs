# useSelectionForFind(_:)

**Framework**: UIKit  
**Kind**: method

Begins a search for the selected content in your app’s interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func useSelectionForFind(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Use Selection For Find command from an editing menu. Your implementation should present the UI for finding textual content in your view and use the selected text for the search.

For example, a view using a find interaction might call [`presentFindNavigator(showingReplace:)`](uifindinteraction/presentfindnavigator(showingreplace:).md) and pass the selected text as the query string.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func find(Any?)](uiresponderstandardeditactions/find(_:).md)
  Begins a search for content in your app’s interface.
- [func findNext(Any?)](uiresponderstandardeditactions/findnext(_:).md)
  Finds the next match in your app’s interface.
- [func findPrevious(Any?)](uiresponderstandardeditactions/findprevious(_:).md)
  Finds the previous match in your app’s interface.
- [func findAndReplace(Any?)](uiresponderstandardeditactions/findandreplace(_:).md)
  Begins a search for content in your app’s interface and provides a replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/useselectionforfind(_:))*