# enqueue(_:completionHandler:)

**Framework**: Videosubscriberaccount  
**Kind**: method

Submits a request for subscriber account information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func enqueue(_ request: VSAccountMetadataRequest, completionHandler: @escaping (VSAccountMetadata?, (any Error)?) -> Void) -> VSAccountManagerResult
```

#### Return Value

Returns a [`VSAccountManagerResult`](vsaccountmanagerresult.md) object that your app can use with [`cancel()`](vsaccountmanagerresult/cancel().md) to cancel the request.

## Parameters

- `request`: A   object that contains the information that your app requests.
- `completionHandler`: The closure that the account manager executes after the request completes. This closure has no return value and takes the following parameters:

## See Also

- [class VSAccountMetadataRequest](vsaccountmetadatarequest.md)
  An object that specifies what subscriber account information your app retrieves.
- [class VSAccountMetadata](vsaccountmetadata.md)
  A collection of information for a subscriber’s account.
- [class VSAccountManagerResult](vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [class VSAccountProviderResponse](vsaccountproviderresponse.md)
  An object that contains the response from the account provider.
- [struct VSAccountProviderAuthenticationScheme](vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanager/enqueue(_:completionhandler:))*