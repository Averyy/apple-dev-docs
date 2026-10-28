# status

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The status code for the response.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- macOS
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var status: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * status;
```

## Discussion

This property is `nil` if the response doesn’t match an existing status type.

## See Also

### Getting Response Info
- [var authenticationScheme: VSAccountProviderAuthenticationScheme](./authenticationscheme.md)
  The authentication scheme type of the response.
- [var body: String?](./body.md)
  The raw response from the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse/status)*