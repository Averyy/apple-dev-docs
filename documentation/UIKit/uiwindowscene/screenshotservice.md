# screenshotService

**Framework**: UIKit  
**Kind**: property

An object that generates a high-fidelity version of your app’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+

## Declaration

```swift
@MainActor
var screenshotService: UIScreenshotService? { get }
```

#### Discussion

When you want to make your scene content available in PDF format, supply a delegate to the [`UIScreenshotService`](uiscreenshotservice.md) object in this property. When the user takes a screenshot involving your scene, the screenshot service asks your delegate to provide the associated PDF data. Your delegate object must conform to the [`UIScreenshotServiceDelegate`](uiscreenshotservicedelegate.md) protocol.

Provide PDF data for your app’s content whenever possible. Providing the data makes it easier and faster for the user to mark up that data later.

## See Also

- [class UIScreenshotService](uiscreenshotservice.md)
  An object that coordinates the creation of PDF screenshots of an app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/screenshotservice)*