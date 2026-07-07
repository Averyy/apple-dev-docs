# VSAppleSubscription

**Framework**: Video Subscriber Account  
**Kind**: struct

An Apple streaming service customer and their subscriptions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
struct VSAppleSubscription
```

## Topics

### Creating an Apple subscription
- [init(customerID: String, productCodes: [String])](vsapplesubscription-swift.struct/init(customerid:productcodes:).md)
  Initializes an Apple subscription object.
### Identifying a subscription
- [var customerID: String](vsapplesubscription-swift.struct/customerid.md)
  The identifier of the customer as previously reported to Apple.
- [var productCodes: [String]](vsapplesubscription-swift.struct/productcodes.md)
  A list of product codes for Apple services the customer subscribes to.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class VSSubscriptionRegistrationCenter](vssubscriptionregistrationcenter.md)
  An object that stores subscription information that the system provides to the Apple TV app.
- [class VSAccountApplicationProvider](vsaccountapplicationprovider.md)
  An object to display app-specific providers in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsapplesubscription-swift.struct)*