# resultOptions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The type of content the system generates for your custom text view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
var resultOptions: UIWritingToolsResultOptions { get }
```

```objc
@property (nonatomic, readonly) UIWritingToolsResultOptions resultOptions;
```

#### Discussion

This property contains the set of options that Writing Tools outputs for your view. Writing Tools takes the value in the [`preferredResultOptions`](./preferredresultoptions.md) property into consideration when determining this value.

## See Also

### Configuring the experience
- [var preferredBehavior: UIWritingToolsBehavior](./preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: UIWritingToolsBehavior](./behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: UIWritingToolsResultOptions](./preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/resultoptions)*