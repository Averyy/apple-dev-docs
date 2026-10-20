# init(localizedDisplayName:identifier:)

**Framework**: Video Subscriber Account  
**Kind**: init  
**Role**: Initializer

Returns an application provider using a given display name and identifier.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS
- tvOS 14.2+
- visionOS 1.0+

## Declaration

```swift
init(localizedDisplayName: String, identifier: String)
```

```objc
- (instancetype) initWithLocalizedDisplayName:(NSString *) localizedDisplayName identifier:(NSString *) identifier;
```

## Parameters

- `localizedDisplayName`: The display name of the provider as it will appear in the list of providers.
- `identifier`: The identifier of the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountapplicationprovider/init(localizeddisplayname:identifier:))*