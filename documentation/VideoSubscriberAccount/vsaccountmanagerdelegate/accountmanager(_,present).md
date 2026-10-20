# accountManager(_:present:)

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate to present an authentication view controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func accountManager(_ accountManager: VSAccountManager, present viewController: UIViewController)
```

```objc
- (void) accountManager:(VSAccountManager *) accountManager presentViewController:(UIViewController *) viewController;
```

#### Discussion

The system calls this method when the `VideoSubscriberAccount` framework requires your app to present an authentication view controller. You must use [`present(_:animated:completion:)`](../../UIKit/uiviewcontroller/present%28_,animated,completion%29.md) to present the view controller before returning from this method.

## Parameters

- `accountManager`: The account manager instance that requests the authentication view controller.
- `viewController`: The view controller your app must present to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerdelegate/accountmanager(_:present:))*