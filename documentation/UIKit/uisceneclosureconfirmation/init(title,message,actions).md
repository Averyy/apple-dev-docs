# init(title:message:actions:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a scene closure confirmation with the provided parameters.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
convenience init(title: String?, message: String?, actions: [UIAlertAction])
```

```objc
+ (instancetype) confirmationWithTitle:(NSString *) title message:(NSString *) message actions:(NSArray<UIAlertAction *> *) actions;
```

## Parameters

- `title`: The title of the confirmation. If not provided, defaults to a generic localized title.
- `message`: Optional descriptive text that provides more details.
- `actions`: Actions to be included in the confirmation dialog. Close and Cancel are shown by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneclosureconfirmation/init(title:message:actions:))*