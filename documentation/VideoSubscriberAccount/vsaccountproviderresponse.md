# VSAccountProviderResponse

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

An object that contains the response from the account provider.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- macOS
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
class VSAccountProviderResponse
```

```objc
@interface VSAccountProviderResponse : NSObject
```

#### Overview

A `VSAccountProviderResponse` object encapsulates the information the account provider sends back to your app, such as authentication scheme type, raw response data, and status code.

## Topics

### Getting Response Info
- [var authenticationScheme: VSAccountProviderAuthenticationScheme](./vsaccountproviderresponse/authenticationscheme.md)
  The authentication scheme type of the response.
- [var body: String?](./vsaccountproviderresponse/body.md)
  The raw response from the provider.
- [var status: String?](./vsaccountproviderresponse/status.md)
  The status code for the response.

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

### Enqueuing requests
- [func enqueue(VSAccountMetadataRequest, completionHandler: (VSAccountMetadata?, (any Error)?) -> Void) -> VSAccountManagerResult](./vsaccountmanager/enqueue%28_,completionhandler%29.md)
  Submits a request for subscriber account information.
- [class VSAccountMetadataRequest](./vsaccountmetadatarequest.md)
  An object that specifies what subscriber account information your app retrieves.
- [class VSAccountMetadata](./vsaccountmetadata.md)
  A collection of information for a subscriber’s account.
- [class VSAccountManagerResult](./vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [struct VSAccountProviderAuthenticationScheme](./vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse)*