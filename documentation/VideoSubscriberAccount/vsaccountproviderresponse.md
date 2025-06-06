# VSAccountProviderResponse

**Framework**: Videosubscriberaccount  
**Kind**: class

An object that contains the response from the account provider.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- macOS ?+
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
class VSAccountProviderResponse
```

#### Overview

A `VSAccountProviderResponse` object encapsulates the information the account provider sends back to your app, such as authentication scheme type, raw response data, and status code.

## Topics

### Getting Response Info
- [var authenticationScheme: VSAccountProviderAuthenticationScheme](vsaccountproviderresponse/authenticationscheme.md)
  The authentication scheme type of the response.
- [var body: String?](vsaccountproviderresponse/body.md)
  The raw response from the provider.
- [var status: String?](vsaccountproviderresponse/status.md)
  The status code for the response.

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

- [func enqueue(VSAccountMetadataRequest, completionHandler: (VSAccountMetadata?, (any Error)?) -> Void) -> VSAccountManagerResult](vsaccountmanager/enqueue(_:completionhandler:).md)
  Submits a request for subscriber account information.
- [class VSAccountMetadataRequest](vsaccountmetadatarequest.md)
  An object that specifies what subscriber account information your app retrieves.
- [class VSAccountMetadata](vsaccountmetadata.md)
  A collection of information for a subscriber’s account.
- [class VSAccountManagerResult](vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [struct VSAccountProviderAuthenticationScheme](vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse)*