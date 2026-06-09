# init(title:message:actions:)

**Framework**: UIKit  
**Kind**: init

Creates a scene closure confirmation with the provided parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(title: String?, message: String?, actions: [UIAlertAction])
```

## Parameters

- `title`: The title of the confirmation. If not provided, defaults to a generic localized title.
- `message`: Optional descriptive text that provides more details.
- `actions`: Actions to be included in the confirmation dialog. Close and Cancel are shown by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneclosureconfirmation/init(title:message:actions:))*