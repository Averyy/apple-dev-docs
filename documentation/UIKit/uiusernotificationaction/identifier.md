# identifier

**Framework**: UIKit  
**Kind**: property

The string that you use internally to identify the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var identifier: String? { get }
```

#### Discussion

The system passes this string to the [`application(_:handleActionWithIdentifier:for:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:for:completionhandler:).md) or [`application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)`](uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:).md) method of the app delegate when the user chooses the action.

## See Also

- [var title: String?](uiusernotificationaction/title.md)
  The localized string to use as the button title for the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiusernotificationaction/identifier)*