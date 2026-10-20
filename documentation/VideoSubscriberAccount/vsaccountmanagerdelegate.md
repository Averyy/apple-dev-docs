# VSAccountManagerDelegate

**Framework**: Video Subscriber Account  
**Kind**: protocol  
**Role**: Protocol

The methods you use to respond to authentication view controller requests.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol VSAccountManagerDelegate : NSObjectProtocol
```

```objc
@protocol VSAccountManagerDelegate <NSObject>
```

#### Overview

Use the [`VSAccountManagerDelegate`](./vsaccountmanagerdelegate.md) methods to aid in displaying and dismissing authentication view controllers.

If the person isn’t authenticated when your app calls [`enqueue(_:completionHandler:)`](./vsaccountmanager/enqueue%28_,completionhandler%29.md) with [`isInterruptionAllowed`](./vsaccountmetadatarequest/isinterruptionallowed.md) set to [`true`](../Swift/true.md), the system sends an authentication view controller to the delegate in the [`accountManager(_:present:)`](./vsaccountmanagerdelegate/accountmanager%28_,present%29.md) method for your app to present to them.

## Topics

### Displaying Authentication Views
- [func accountManager(VSAccountManager, present: UIViewController)](./vsaccountmanagerdelegate/accountmanager%28_,present%29.md)
  Tells the delegate to present an authentication view controller.
### Dismissing Authentication Views
- [func accountManager(VSAccountManager, dismiss: UIViewController)](./vsaccountmanagerdelegate/accountmanager%28_,dismiss%29.md)
  Tells the delegate to dismiss an authentication view controller.
### Supporting Degradation Scenarios
- [func accountManager(VSAccountManager, shouldAuthenticateAccountProviderWithIdentifier: String) -> Bool](./vsaccountmanagerdelegate/accountmanager%28_,shouldauthenticateaccountproviderwithidentifier%29.md)
  Asks the delegate whether to authenticate the user with the selected provider.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to account manager requests
- [var delegate: (any VSAccountManagerDelegate)?](./vsaccountmanager/delegate.md)
  The delegate of the account manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerdelegate)*