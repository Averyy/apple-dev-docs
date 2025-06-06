# barStyle

**Framework**: UIKit  
**Kind**: property

The tab bar style that specifies its appearance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barStyle: UIBarStyle { get set }
```

#### Discussion

This property determines whether the tab bar uses a dark or light visual style when no background image or tint color is specified. Together with the [`isTranslucent`](uitabbar/istranslucent.md) property, this property defines the default visual style of the tab bar. Set this property to the value that best matches the style of your interface. For a list of possible values, see [`UIBarStyle`](uibarstyle.md). The default value of this property is [`UIBarStyle.default`](uibarstyle/default.md).

## See Also

- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/barstyle)*