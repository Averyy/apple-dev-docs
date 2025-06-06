# pasteAndSearch(_:)

**Framework**: UIKit  
**Kind**: method

Pastes the current contents of the pasteboard into your app’s interface and performs a search.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pasteAndSearch(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Paste and Search command from an editing menu. Your implementation should read the data from the pasteboard and begin a search based on the content.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func cut(Any?)](uiresponderstandardeditactions/cut(_:).md)
  Removes the selected content and writes the data for it to the pasteboard.
- [func copy(Any?)](uiresponderstandardeditactions/copy(_:).md)
  Copies the selected content to the pasteboard.
- [func paste(Any?)](uiresponderstandardeditactions/paste(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface.
- [func pasteAndGo(Any?)](uiresponderstandardeditactions/pasteandgo(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [func pasteAndMatchStyle(Any?)](uiresponderstandardeditactions/pasteandmatchstyle(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [func delete(Any?)](uiresponderstandardeditactions/delete(_:).md)
  Removes the selected content from your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/pasteandsearch(_:))*