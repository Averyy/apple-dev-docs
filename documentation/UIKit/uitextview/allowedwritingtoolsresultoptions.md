# allowedWritingToolsResultOptions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The type of content Writing Tools generates for your text view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
var allowedWritingToolsResultOptions: UIWritingToolsResultOptions { get set }
```

```objc
@property UIWritingToolsResultOptions allowedWritingToolsResultOptions;
```

#### Discussion

Text views support most types of generated content. However, if you set this property to a value that includes the [`table`](../uiwritingtoolsresultoptions/table.md) option, UIKit raises [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md).

## See Also

### Getting the Writing Tools configuration
- [var writingToolsBehavior: UIWritingToolsBehavior](./writingtoolsbehavior.md)
  The level of Writing Tools support to use in the text view.
- [var isWritingToolsActive: Bool](./iswritingtoolsactive.md)
  A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [var writingToolsCoordinator: UIWritingToolsCoordinator](./writingtoolscoordinator.md)
  The object that coordinates interactions between Writing Tools and the text view.
- [var subclassForWritingToolsCoordinator: AnyClass](./subclassforwritingtoolscoordinator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/allowedwritingtoolsresultoptions)*