# VSAccountApplicationProvider

**Framework**: Video Subscriber Account  
**Kind**: class

An object to display app-specific providers in your app.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- macOS ?+
- tvOS 14.2+
- visionOS 1.0+

## Declaration

```swift
class VSAccountApplicationProvider
```

#### Overview

The `VSAccountApplicationProvider` object represents an app account provider to be added to the list of already available system TV providers in your app.

## Topics

### Creating an application provider
- [init(localizedDisplayName: String, identifier: String)](vsaccountapplicationprovider/init(localizeddisplayname:identifier:).md)
  Returns an application provider using a given display name and identifier.
### Application provider details
- [var identifier: String](vsaccountapplicationprovider/identifier.md)
  A string that identifies a provider.
- [var localizedDisplayName: String](vsaccountapplicationprovider/localizeddisplayname.md)
  The display name of the provider as it will appear in the list of providers.

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
- [class VSSubscriptionRegistrationCenter](vssubscriptionregistrationcenter.md)
  An object that stores subscription information that the system provides to the Apple TV app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountapplicationprovider)*