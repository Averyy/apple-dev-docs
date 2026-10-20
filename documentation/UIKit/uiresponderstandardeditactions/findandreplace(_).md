# findAndReplace(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Begins a search for content in your app’s interface and provides a replacement.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func findAndReplace(_ sender: Any?)
```

```objc
- (void) findAndReplace:(id) sender;
```

#### Discussion

UIKit calls this method when the user selects the Find and Replace command from an editing menu. Your implementation should present the UI for finding and replacing textual content in your view.

For example, a view using a find interaction might call [`presentFindNavigator(showingReplace:)`](../uifindinteraction/presentfindnavigator%28showingreplace%29.md) to present the system find panel.

## Parameters

- `sender`: The object calling this method.

## See Also

### Handling find and replace commands
- [func find(Any?)](./find%28_%29.md)
  Begins a search for content in your app’s interface.
- [func findNext(Any?)](./findnext%28_%29.md)
  Finds the next match in your app’s interface.
- [func findPrevious(Any?)](./findprevious%28_%29.md)
  Finds the previous match in your app’s interface.
- [func useSelectionForFind(Any?)](./useselectionforfind%28_%29.md)
  Begins a search for the selected content in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/findandreplace(_:))*