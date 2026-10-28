# authenticationScheme

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The authentication scheme type of the response.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- macOS
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var authenticationScheme: VSAccountProviderAuthenticationScheme { get }
```

```objc
@property (nonatomic, copy, readonly) VSAccountProviderAuthenticationScheme authenticationScheme;
```

## Discussion

This property identifies the authentication scheme the account provider used to construct the response. For a list of types, see [`VSAccountProviderAuthenticationScheme`](../vsaccountproviderauthenticationscheme.md).

## See Also

### Getting Response Info
- [var body: String?](./body.md)
  The raw response from the provider.
- [var status: String?](./status.md)
  The status code for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse/authenticationscheme)*