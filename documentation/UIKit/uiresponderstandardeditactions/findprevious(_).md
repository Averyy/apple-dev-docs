# findPrevious(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Finds the previous match in your app’s interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func findPrevious(_ sender: Any?)
```

```objc
- (void) findPrevious:(id) sender;
```

## Discussion

UIKit calls this method when the user selects the Find Previous command from an editing menu. Your implementation should highlight the previous result in the UI for finding textual content in your view.

For example, a view using a find interaction might call [`highlightNextResult(in:)`](../uifindsession/highlightnextresult%28in%29.md) to update the find session.

## Parameters

- `sender`: The object calling this method.

## See Also

### Handling find and replace commands
- [func find(Any?)](./find%28_%29.md)
  Begins a search for content in your app’s interface.
- [func findNext(Any?)](./findnext%28_%29.md)
  Finds the next match in your app’s interface.
- [func findAndReplace(Any?)](./findandreplace%28_%29.md)
  Begins a search for content in your app’s interface and provides a replacement.
- [func useSelectionForFind(Any?)](./useselectionforfind%28_%29.md)
  Begins a search for the selected content in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/findprevious(_:))*