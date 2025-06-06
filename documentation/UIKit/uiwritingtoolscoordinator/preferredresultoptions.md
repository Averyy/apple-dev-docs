# preferredResultOptions

**Framework**: UIKit  
**Kind**: property

The type of content you allow Writing Tools to generate for your custom text view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var preferredResultOptions: UIWritingToolsResultOptions { get set }
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

Writing Tools can create plain text or rich text, and it can format text using lists or tables as needed. If your view doesn’t support specific types of content, specify the types you do support in this property. The default value of this property is `UIWritingToolsResultOptions/default`, which lets the system determine the type of content to generate.

## See Also

- [var preferredBehavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var resultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/preferredresultoptions)*