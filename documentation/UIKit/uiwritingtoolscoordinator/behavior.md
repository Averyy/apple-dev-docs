# behavior

**Framework**: UIKit  
**Kind**: property

The actual level of Writing Tools support the system provides for your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var behavior: UIWritingToolsBehavior { get }
```

#### Discussion

The system chooses this value based on the device capabilities, and takes the value in the [`preferredBehavior`](uiwritingtoolscoordinator/preferredbehavior.md) property into consideration when making the choice. The value in this property is never the default option, and is instead one of the specific options such as [`UIWritingToolsBehavior.none`](uiwritingtoolsbehavior/none.md), [`UIWritingToolsBehavior.limited`](uiwritingtoolsbehavior/limited.md), or [`UIWritingToolsBehavior.complete`](uiwritingtoolsbehavior/complete.md).

## See Also

- [var preferredBehavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var preferredResultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/behavior)*