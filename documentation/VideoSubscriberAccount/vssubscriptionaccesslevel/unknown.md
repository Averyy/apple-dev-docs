# VSSubscriptionAccessLevel.unknown

**Framework**: Video Subscriber Account  
**Kind**: case  
**Role**: Case

The default access level.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 11.0+ - Deprecated in 18.0
- macOS
- tvOS 11.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use VSUserAccount and VSUserAccountType instead.

## Declaration

```swift
case unknown
```

```c
VSSubscriptionAccessLevelUnknown
```

#### Discussion

> ⚠️ **Warning**:  An error occurs if you try to set a `VSSubscriptionAccessLevel` type to this value.

## See Also

### Subscription Tiers
- [VSSubscriptionAccessLevel.freeWithAccount](./freewithaccount.md)
  The user has access to free content with a valid account.
- [VSSubscriptionAccessLevel.paid](./paid.md)
  The user has access to content that requires a paid subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionaccesslevel/unknown)*