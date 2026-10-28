# pasteAndGo(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func pasteAndGo(_ sender: Any?)
```

```objc
- (void) pasteAndGo:(id) sender;
```

## Discussion

UIKit calls this method when the user selects the Paste and Go command from an editing menu. Your implementation should read the data from the pasteboard, add the resulting content to your interface, and begin navigating to the entity the content references.

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
- [func pasteAndMatchStyle(Any?)](./pasteandmatchstyle%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [func pasteAndSearch(Any?)](./pasteandsearch%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [func delete(Any?)](./delete%28_%29.md)
  Removes the selected content from your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/pasteandgo(_:))*