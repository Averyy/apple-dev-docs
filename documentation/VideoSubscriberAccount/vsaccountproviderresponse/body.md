# body

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The raw response from the provider.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- macOS
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var body: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * body;
```

## Discussion

This property is `nil` if the response contains security-sensitive information.

## See Also

### Getting Response Info
- [var authenticationScheme: VSAccountProviderAuthenticationScheme](./authenticationscheme.md)
  The authentication scheme type of the response.
- [var status: String?](./status.md)
  The status code for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderresponse/body)*