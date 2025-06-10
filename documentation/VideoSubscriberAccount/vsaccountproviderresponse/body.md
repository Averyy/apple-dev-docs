# body

**Framework**: Video Subscriber Account  
**Kind**: property

The raw response from the provider.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- macOS ?+
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var body: String? { get }
```

#### Discussion

This property is `nil` if the response contains security-sensitive information.

## See Also

- [var authenticationScheme: VSAccountProviderAuthenticationScheme](vsaccountproviderresponse/authenticationscheme.md)
  The authentication scheme type of the response.
- [var status: String?](vsaccountproviderresponse/status.md)
  The status code for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse/body)*