# behavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The actual level of Writing Tools support the system provides for your view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
var behavior: UIWritingToolsBehavior { get }
```

```objc
@property (nonatomic, readonly) UIWritingToolsBehavior behavior;
```

## Discussion

The system chooses this value based on the device capabilities, and takes the value in the [`preferredBehavior`](./preferredbehavior.md) property into consideration when making the choice. The value in this property is never the default option, and is instead one of the specific options such as [`UIWritingToolsBehavior.none`](../uiwritingtoolsbehavior/none.md), [`UIWritingToolsBehavior.limited`](../uiwritingtoolsbehavior/limited.md), or [`UIWritingToolsBehavior.complete`](../uiwritingtoolsbehavior/complete.md).

## See Also

### Configuring the experience
- [var preferredBehavior: UIWritingToolsBehavior](./preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var preferredResultOptions: UIWritingToolsResultOptions](./preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: UIWritingToolsResultOptions](./resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/behavior)*