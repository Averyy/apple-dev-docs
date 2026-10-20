# accountManager(_:dismiss:)

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate to dismiss an authentication view controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func accountManager(_ accountManager: VSAccountManager, dismiss viewController: UIViewController)
```

```objc
- (void) accountManager:(VSAccountManager *) accountManager dismissViewController:(UIViewController *) viewController;
```

#### Discussion

The system calls this method when the `VideoSubscriberAccount` framework requires your app to dismiss an authentication view controller. You must use [`dismiss(animated:completion:)`](../../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) to dismiss the view controller before returning from this method.

## Parameters

- `accountManager`: The account manager instance that requests to dismiss the authentication view controller.
- `viewController`: The view controller that your app must dismiss.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerdelegate/accountmanager(_:dismiss:))*