# VSSubscriptionRegistrationCenter

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

An object that stores subscription information that the system provides to the Apple TV app.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- iPadOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- Mac Catalyst 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- macOS
- tvOS 11.0+ - Deprecated in 18.0 (renamed: VSUserAccountManager)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: VSUserAccountManager)

## Declaration

```swift
class VSSubscriptionRegistrationCenter
```

```objc
@interface VSSubscriptionRegistrationCenter : NSObject
```

## Overview

Use the methods in this class to retrieve the default registration center object and set the user’s current subscription for your app. This subscription informs the Apple TV app of the user’s access level and tiers.

## Topics

### Setting the Current Subscription
- [func setCurrentSubscription(VSSubscription?)](./vssubscriptionregistrationcenter/setcurrentsubscription%28_%29.md)
  Sets the subscription information for the current user.
### Getting the Default Registration Center
- [class func `default`() -> VSSubscriptionRegistrationCenter](./vssubscriptionregistrationcenter/default%28%29.md)
  Returns the default subscription registration center object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### TV app integration
- [struct VSAppleSubscription](./vsapplesubscription-swift.struct.md)
  An Apple streaming service customer and their subscriptions.
- [class VSAccountApplicationProvider](./vsaccountapplicationprovider.md)
  An object to display app-specific providers in your app.
- [VSAppleSubscription](./vsapplesubscription-c.class.md)
  An Apple streaming service customer and their subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionregistrationcenter)*