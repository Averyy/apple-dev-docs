# resultOptions

**Framework**: UIKit  
**Kind**: property

The type of content the system generates for your custom text view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var resultOptions: UIWritingToolsResultOptions { get }
```

#### Discussion

This property contains the set of options that Writing Tools outputs for your view. Writing Tools takes the value in the [`preferredResultOptions`](uiwritingtoolscoordinator/preferredresultoptions.md) property into consideration when determining this value.

## See Also

- [var preferredBehavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/resultoptions)*