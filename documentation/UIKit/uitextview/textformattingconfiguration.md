# textFormattingConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

For text views that have flag `allowsEditingTextAttributes` set, this configuration will be used for `UITextFormattingViewController` when its presentation is requested.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var textFormattingConfiguration: UITextFormattingViewController.Configuration? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UITextFormattingViewControllerConfiguration * textFormattingConfiguration;
```

#### Discussion

It has a non-nil default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textformattingconfiguration)*