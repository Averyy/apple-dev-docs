# default()

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Type Method

Returns the default subscription registration center object.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- iPadOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- Mac Catalyst 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- macOS
- tvOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: VSUserAccountManager)

## Declaration

```swift
class func `default`() -> VSSubscriptionRegistrationCenter
```

```objc
+ (VSSubscriptionRegistrationCenter *) defaultSubscriptionRegistrationCenter;
```

#### Return Value

This method returns a [`VSSubscriptionRegistrationCenter`](../vssubscriptionregistrationcenter.md) object that refers to the default registration center.

#### Discussion

Use the object this method returns to tell the system what content the user is able to access within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionregistrationcenter/default())*