# VSSubscriptionRegistrationCenter

**Framework**: Video Subscriber Account  
**Kind**: class

An object that stores subscription information that the system provides to the Apple TV app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS ?+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VSSubscriptionRegistrationCenter
```

#### Overview

Use the methods in this class to retrieve the default registration center object and set the user’s current subscription for your app. This subscription informs the Apple TV app of the user’s access level and tiers.

## Topics

### Setting the Current Subscription
- [func setCurrentSubscription(VSSubscription?)](vssubscriptionregistrationcenter/setcurrentsubscription(_:).md)
  Sets the subscription information for the current user.
### Getting the Default Registration Center
- [class func `default`() -> VSSubscriptionRegistrationCenter](vssubscriptionregistrationcenter/default.md)
  Returns the default subscription registration center object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct VSAppleSubscription](vsapplesubscription-swift.struct.md)
  An Apple streaming service customer and their subscriptions.
- [class VSAccountApplicationProvider](vsaccountapplicationprovider.md)
  An object to display app-specific providers in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionregistrationcenter)*