# preferredBehavior

**Framework**: UIKit  
**Kind**: property

The level of Writing Tools support you want the system to provide for your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var preferredBehavior: UIWritingToolsBehavior { get set }
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

Use this property to request an inline or panel-based experience, or to disable Writing Tools for your view altogether. The default value of this property is [`UIWritingToolsBehavior.default`](uiwritingtoolsbehavior/default.md).

## See Also

- [var behavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/preferredbehavior)*