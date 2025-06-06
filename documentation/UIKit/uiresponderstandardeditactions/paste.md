# paste(_:)

**Framework**: UIKit  
**Kind**: method

Pastes the current contents of the pasteboard into your app’s interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func paste(_ sender: Any?)
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)

#### Discussion

UIKit calls this method when the user selects the Paste command from an editing menu. Your implementation should read the data from the pasteboard and add the resulting content to your interface.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func cut(Any?)](uiresponderstandardeditactions/cut(_:).md)
  Removes the selected content and writes the data for it to the pasteboard.
- [func copy(Any?)](uiresponderstandardeditactions/copy(_:).md)
  Copies the selected content to the pasteboard.
- [func pasteAndGo(Any?)](uiresponderstandardeditactions/pasteandgo(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [func pasteAndMatchStyle(Any?)](uiresponderstandardeditactions/pasteandmatchstyle(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [func pasteAndSearch(Any?)](uiresponderstandardeditactions/pasteandsearch(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [func delete(Any?)](uiresponderstandardeditactions/delete(_:).md)
  Removes the selected content from your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/paste(_:))*