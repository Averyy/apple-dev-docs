# VSAccountApplicationProvider

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

An object to display app-specific providers in your app.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS
- tvOS 14.2+
- visionOS 1.0+

## Declaration

```swift
class VSAccountApplicationProvider
```

```objc
@interface VSAccountApplicationProvider : NSObject
```

#### Overview

The `VSAccountApplicationProvider` object represents an app account provider to be added to the list of already available system TV providers in your app.

## Topics

### Creating an application provider
- [init(localizedDisplayName: String, identifier: String)](./vsaccountapplicationprovider/init%28localizeddisplayname,identifier%29.md)
  Returns an application provider using a given display name and identifier.
### Application provider details
- [var identifier: String](./vsaccountapplicationprovider/identifier.md)
  A string that identifies a provider.
- [var localizedDisplayName: String](./vsaccountapplicationprovider/localizeddisplayname.md)
  The display name of the provider as it will appear in the list of providers.

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
- [class VSSubscriptionRegistrationCenter](./vssubscriptionregistrationcenter.md)
  An object that stores subscription information that the system provides to the Apple TV app.
- [VSAppleSubscription](./vsapplesubscription-c.class.md)
  An Apple streaming service customer and their subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountapplicationprovider)*