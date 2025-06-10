# UIWritingToolsCoordinator.ContextScope.userSelection

**Framework**: UIKit  
**Kind**: case

An option to provide only the view’s currently selected text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case userSelection
```

#### Discussion

With this option, include the selected text in your context object, along with some additional text before and after the selection. When performing changes inline with your view’s content, Writing Tools applies animations only to the selected text.

## See Also

- [UIWritingToolsCoordinator.ContextScope.fullDocument](uiwritingtoolscoordinator/contextscope/fulldocument.md)
  An option to provide all of your view’s text.
- [UIWritingToolsCoordinator.ContextScope.visibleArea](uiwritingtoolscoordinator/contextscope/visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope/userselection)*