# tierIdentifiers

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A list of content from your catalog that the subscriber can access.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 11.0+ - Deprecated in 18.0
- macOS
- tvOS 11.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use VSUserAccount instead.

## Declaration

```swift
var tierIdentifiers: [String]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSArray<NSString *> * tierIdentifiers;
```

#### Discussion

You should only use values that are in your availability feed’s tier restrictions.

## See Also

### Setting Subscription Details
- [var accessLevel: VSSubscriptionAccessLevel](./accesslevel.md)
  The subscriber’s level of access to your catalog of content.
- [enum VSSubscriptionAccessLevel](../vssubscriptionaccesslevel.md)
  Constants representing a subscriber’s level of access to your content.
- [var billingIdentifier: String?](./billingidentifier.md)
  The subscriber’s billing group.
- [var expirationDate: Date!](./expirationdate.md)
  The date when the user’s subscription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription/tieridentifiers)*