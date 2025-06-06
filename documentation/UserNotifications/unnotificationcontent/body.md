# body

**Framework**: Usernotifications  
**Kind**: property

The localized text that provides the notification’s main content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var body: String { get }
```

#### Discussion

The body text contains the final text that you want to display. If your app isn’t authorized to display alert-based notifications, the system ignores this property.

If you specified two percent symbols (`%%`) in the message body, the system replaces it with a single percent symbol (`%`). The system strips all other printf style escape characters from your string prior to display.

## See Also

- [var title: String](unnotificationcontent/title.md)
  The localized text that provides the notification’s primary description.
- [var subtitle: String](unnotificationcontent/subtitle.md)
  The localized text that provides the notification’s secondary description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/body)*