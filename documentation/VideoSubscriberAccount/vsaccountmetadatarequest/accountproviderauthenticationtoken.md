# accountProviderAuthenticationToken

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

An authentication session token that your app sends to the account provider.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var accountProviderAuthenticationToken: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * accountProviderAuthenticationToken;
```

#### Discussion

Only TV provider apps use this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/accountproviderauthenticationtoken)*