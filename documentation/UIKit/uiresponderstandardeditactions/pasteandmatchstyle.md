# pasteAndMatchStyle(_:)

**Framework**: UIKit  
**Kind**: method

Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pasteAndMatchStyle(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Paste command from an editing menu. Your implementation should read the data from the pasteboard and add the resulting content to your interface using the target’s current text style.

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
- [func pasteAndSearch(Any?)](uiresponderstandardeditactions/pasteandsearch(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [func delete(Any?)](uiresponderstandardeditactions/delete(_:).md)
  Removes the selected content from your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/pasteandmatchstyle(_:))*