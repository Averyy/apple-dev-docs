# VSSubscriptionAccessLevel.paid

**Framework**: Video Subscriber Account  
**Kind**: case  
**Role**: Case

The user has access to content that requires a paid subscription.

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
case paid
```

```c
VSSubscriptionAccessLevelPaid
```

## Discussion

This value corresponds to content in your availability feed with the *subscription* offering type. Subscribers with this access level can also access free content.

## See Also

### Subscription Tiers
- [VSSubscriptionAccessLevel.freeWithAccount](./freewithaccount.md)
  The user has access to free content with a valid account.
- [VSSubscriptionAccessLevel.unknown](./unknown.md)
  The default access level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionaccesslevel/paid)*