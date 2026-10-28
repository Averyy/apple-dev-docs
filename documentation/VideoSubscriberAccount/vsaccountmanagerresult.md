# VSAccountManagerResult

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

An object that represents a request made for subscriber account information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class VSAccountManagerResult
```

```objc
@interface VSAccountManagerResult : NSObject
```

## Overview

The system returns this object to your app when you app calls [`enqueue(_:completionHandler:)`](./vsaccountmanager/enqueue%28_,completionhandler%29.md). Use this object to cancel the request with [`cancel()`](./vsaccountmanagerresult/cancel%28%29.md) while the request is in progress.

## Topics

### Cancelling a Request
- [func cancel()](./vsaccountmanagerresult/cancel%28%29.md)
  Cancels an in-progress request for subscriber account information.

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
- [class VSAccountProviderResponse](./vsaccountproviderresponse.md)
  An object that contains the response from the account provider.
- [struct VSAccountProviderAuthenticationScheme](./vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerresult)*