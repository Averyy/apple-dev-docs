# UIWritingToolsCoordinator.ContextScope.fullDocument

**Framework**: UIKit  
**Kind**: case

An option to provide all of your view’s text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
case fullDocument
```

#### Discussion

With this option, include all of the text your view manages. If your view has multiple text storage objects, create a separate context object for each one.

## See Also

- [UIWritingToolsCoordinator.ContextScope.userSelection](uiwritingtoolscoordinator/contextscope/userselection.md)
  An option to provide only the view’s currently selected text.
- [UIWritingToolsCoordinator.ContextScope.visibleArea](uiwritingtoolscoordinator/contextscope/visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope/fulldocument)*