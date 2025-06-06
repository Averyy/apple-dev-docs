# accountManager(_:dismiss:)

**Framework**: Videosubscriberaccount  
**Kind**: method  
**Required**: Yes

Tells the delegate to dismiss an authentication view controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func accountManager(_ accountManager: VSAccountManager, dismiss viewController: UIViewController)
```

#### Discussion

The system calls this method when the `VideoSubscriberAccount` framework requires your app to dismiss an authentication view controller. You must use [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) to dismiss the view controller before returning from this method.

## Parameters

- `accountManager`: The account manager instance that requests to dismiss the authentication view controller.
- `viewController`: The view controller that your app must dismiss.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerdelegate/accountmanager(_:dismiss:))*