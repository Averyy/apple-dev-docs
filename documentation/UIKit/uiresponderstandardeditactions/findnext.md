# findNext(_:)

**Framework**: UIKit  
**Kind**: method

Finds the next match in your app’s interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func findNext(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Find Next command from an editing menu. Your implementation should highlight the next result in the UI for finding textual content in your view.

For example, a view using a find interaction might call [`highlightNextResult(in:)`](uifindsession/highlightnextresult(in:).md) to update the find session.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func find(Any?)](uiresponderstandardeditactions/find(_:).md)
  Begins a search for content in your app’s interface.
- [func findPrevious(Any?)](uiresponderstandardeditactions/findprevious(_:).md)
  Finds the previous match in your app’s interface.
- [func findAndReplace(Any?)](uiresponderstandardeditactions/findandreplace(_:).md)
  Begins a search for content in your app’s interface and provides a replacement.
- [func useSelectionForFind(Any?)](uiresponderstandardeditactions/useselectionforfind(_:).md)
  Begins a search for the selected content in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/findnext(_:))*