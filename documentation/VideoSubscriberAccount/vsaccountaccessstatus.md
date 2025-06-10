# VSAccountAccessStatus

**Framework**: Video Subscriber Account  
**Kind**: enum

Constants that represent your app’s access status to the user’s subscription information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum VSAccountAccessStatus
```

## Topics

### Statuses
- [VSAccountAccessStatus.denied](vsaccountaccessstatus/denied.md)
  The user denied the app access to subscription information.
- [VSAccountAccessStatus.granted](vsaccountaccessstatus/granted.md)
  The user allowed the app to access subscription information.
- [VSAccountAccessStatus.notDetermined](vsaccountaccessstatus/notdetermined.md)
  The user hasn’t chosen whether to allow the app to access subscription information.
- [VSAccountAccessStatus.restricted](vsaccountaccessstatus/restricted.md)
  The app isn’t allowed to access subscription information.
### Initializers
- [init?(rawValue: Int)](vsaccountaccessstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func checkAccessStatus(options: [VSCheckAccessOption : Any], completionHandler: (VSAccountAccessStatus, (any Error)?) -> Void)](vsaccountmanager/checkaccessstatus(options:completionhandler:).md)
  Checks your app’s access to user subscription information, and requests access if needed.
- [struct VSCheckAccessOption](vscheckaccessoption.md)
  The options your app uses when checking access status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountaccessstatus)*