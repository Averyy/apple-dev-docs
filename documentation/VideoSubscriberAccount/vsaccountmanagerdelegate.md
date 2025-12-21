# VSAccountManagerDelegate

**Framework**: Video Subscriber Account  
**Kind**: protocol

The methods you use to respond to authentication view controller requests.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol VSAccountManagerDelegate : NSObjectProtocol
```

#### Overview

Use the [`VSAccountManagerDelegate`](vsaccountmanagerdelegate.md) methods to aid in displaying and dismissing authentication view controllers.

If the person isn’t authenticated when your app calls [`enqueue(_:completionHandler:)`](vsaccountmanager/enqueue(_:completionhandler:).md) with [`isInterruptionAllowed`](vsaccountmetadatarequest/isinterruptionallowed.md) set to [`true`](https://developer.apple.com/documentation/Swift/true), the system sends an authentication view controller to the delegate in the [`accountManager(_:present:)`](vsaccountmanagerdelegate/accountmanager(_:present:).md) method for your app to present to them.

## Topics

### Displaying Authentication Views
- [func accountManager(VSAccountManager, present: UIViewController)](vsaccountmanagerdelegate/accountmanager(_:present:).md)
  Tells the delegate to present an authentication view controller.
### Dismissing Authentication Views
- [func accountManager(VSAccountManager, dismiss: UIViewController)](vsaccountmanagerdelegate/accountmanager(_:dismiss:).md)
  Tells the delegate to dismiss an authentication view controller.
### Supporting Degradation Scenarios
- [func accountManager(VSAccountManager, shouldAuthenticateAccountProviderWithIdentifier: String) -> Bool](vsaccountmanagerdelegate/accountmanager(_:shouldauthenticateaccountproviderwithidentifier:).md)
  Asks the delegate whether to authenticate the user with the selected provider.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any VSAccountManagerDelegate)?](vsaccountmanager/delegate.md)
  The delegate of the account manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerdelegate)*