# initWithAccountType:updateURL:

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Creates a user account object with a URL for account update requests.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithAccountType:(VSUserAccountType) accountType updateURL:(NSURL *) url;
```

## Return Value

A user account object with a URL for account update requests.

## Parameters

- `accountType`: A constant that represents whether a user has access to paid content.
- `url`: A URL that points to the application’s JavaScript endpoint for update requests.

## See Also

### Creating user accounts
- [VSUserAccountType](../vsuseraccounttype.md)
  Constants that represent whether a user has access to paid content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-c.class/initwithaccounttype:updateurl:)*