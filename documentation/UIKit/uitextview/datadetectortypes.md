# dataDetectorTypes

**Framework**: UIKit  
**Kind**: property

The types of data that convert to tappable URLs in the text view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var dataDetectorTypes: UIDataDetectorTypes { get set }
```

#### Discussion

You can use this property to specify the types of data (phone numbers, `http` links, and so on) that should be automatically converted to URLs in the text view. When tapped, the text view opens the application responsible for handling the URL type and passes it the URL. Note that data detection does not occur if the text view’s [`isEditable`](uitextview/iseditable.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [struct UIDataDetectorTypes](uidatadetectortypes.md)
  Constants that define the types of information to detect in text-based content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/datadetectortypes)*