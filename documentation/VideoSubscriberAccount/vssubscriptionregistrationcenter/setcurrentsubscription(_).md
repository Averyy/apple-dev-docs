# setCurrentSubscription(_:)

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Sets the subscription information for the current user.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- iPadOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- Mac Catalyst 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- macOS
- tvOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: VSUserAccountManager)

## Declaration

```swift
func setCurrentSubscription(_ currentSubscription: VSSubscription?)
```

```objc
- (void) setCurrentSubscription:(VSSubscription *) currentSubscription;
```

#### Discussion

Your app uses this method to set a subscription when the subscriber first authenticates or when their subscription changes.

When the subscriber signs out or loses access to subscription content, your app calls this method with a value of `nil`.

Call this method as needed to update the subscription, such as when you confirm the validity of the subscription, or in response to app lifecycle events when your app becomes active. The system can use this activity as a hint that the user is actively using the subscription.

The system throws an exception if you try to set the current subscription to an unknown access level. Don’t set a subscription if the user only has access to free content.

## Parameters

- `currentSubscription`: A [`VSSubscription`](../vssubscription.md) object that contains the subscription information to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionregistrationcenter/setcurrentsubscription(_:))*