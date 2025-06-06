# delete(_:)

**Framework**: UIKit  
**Kind**: method

Removes the selected content from your interface.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func delete(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Delete command from an editing menu. Your implementation should remove the selected content from your interface.

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
- [func pasteAndSearch(Any?)](uiresponderstandardeditactions/pasteandsearch(_:).md)
  Pastes the current contents of the pasteboard into your app’s interface and performs a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/delete(_:))*