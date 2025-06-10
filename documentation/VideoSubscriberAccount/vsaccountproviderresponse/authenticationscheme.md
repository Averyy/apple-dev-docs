# authenticationScheme

**Framework**: Video Subscriber Account  
**Kind**: property

The authentication scheme type of the response.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- macOS ?+
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var authenticationScheme: VSAccountProviderAuthenticationScheme { get }
```

#### Discussion

This property identifies the authentication scheme the account provider used to construct the response. For a list of types, see [`VSAccountProviderAuthenticationScheme`](vsaccountproviderauthenticationscheme.md).

## See Also

- [var body: String?](vsaccountproviderresponse/body.md)
  The raw response from the provider.
- [var status: String?](vsaccountproviderresponse/status.md)
  The status code for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse/authenticationscheme)*