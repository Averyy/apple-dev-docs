# delete(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the selected content from your interface.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func delete(_ sender: Any?)
```

```objc
- (void) delete:(id) sender;
```

#### Discussion

UIKit calls this method when the user selects the Delete command from an editing menu. Your implementation should remove the selected content from your interface.

## Parameters

- `sender`: The object calling this method.

## See Also

### Handling copy, cut, paste, and delete commands
- [func cut(Any?)](./cut%28_%29.md)
  Removes the selected content and writes the data for it to the pasteboard.
- [func copy(Any?)](./copy%28_%29.md)
  Copies the selected content to the pasteboard.
- [func paste(Any?)](./paste%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface.
- [func pasteAndGo(Any?)](./pasteandgo%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [func pasteAndMatchStyle(Any?)](./pasteandmatchstyle%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [func pasteAndSearch(Any?)](./pasteandsearch%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface and performs a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/delete(_:))*