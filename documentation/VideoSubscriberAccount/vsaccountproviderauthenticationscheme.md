# VSAccountProviderAuthenticationScheme

**Framework**: Video Subscriber Account  
**Kind**: struct  
**Role**: Structure

Authentication schemes for account provider requests and responses.

**Availability**:
- iOS
- iPadOS
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct VSAccountProviderAuthenticationScheme
```

```c
typedef NSString * VSAccountProviderAuthenticationScheme;
```

#### Discussion

If the minimum version your app supports is outside the availability of the [`VSAccountProviderAuthenticationScheme`](./vsaccountproviderauthenticationscheme.md) values, you must create an authentication scheme value using the raw string.

```swift
let request = VSAccountMetadataRequest()
// ...
if #available(iOS 13.0, *) {
  request.supportedAuthenticationSchemes = [.api]
} else {
  request.supportedAuthenticationSchemes = [VSAccountProviderAuthenticationScheme("API")]
}
```

The following table shows the raw strings for the [`VSAccountProviderAuthenticationScheme`](./vsaccountproviderauthenticationscheme.md) values.

| Scheme | Raw Value |
| --- | --- |
| saml | “SAML” |
| api | “API” |

## Topics

### Creating an Authentication Scheme
- [init(String)](./vsaccountproviderauthenticationscheme/init%28_%29.md)
  Creates a new authentication scheme with the specified string.
- [init(rawValue: String)](./vsaccountproviderauthenticationscheme/init%28rawvalue%29.md)
  Creates a new authentication scheme with the specified raw value.
### Authentication Scheme Types
- [static let saml: VSAccountProviderAuthenticationScheme](./vsaccountproviderauthenticationscheme/saml.md)
  Represents a SAML authentication scheme.
- [static let api: VSAccountProviderAuthenticationScheme](./vsaccountproviderauthenticationscheme/api.md)
  Represents any authentication scheme.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enqueuing requests
- [func enqueue(VSAccountMetadataRequest, completionHandler: (VSAccountMetadata?, (any Error)?) -> Void) -> VSAccountManagerResult](./vsaccountmanager/enqueue%28_,completionhandler%29.md)
  Submits a request for subscriber account information.
- [class VSAccountMetadataRequest](./vsaccountmetadatarequest.md)
  An object that specifies what subscriber account information your app retrieves.
- [class VSAccountMetadata](./vsaccountmetadata.md)
  A collection of information for a subscriber’s account.
- [class VSAccountManagerResult](./vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [class VSAccountProviderResponse](./vsaccountproviderresponse.md)
  An object that contains the response from the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderauthenticationscheme)*