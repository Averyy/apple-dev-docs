# VSUserAccountManager.QueryOptions

**Framework**: Video Subscriber Account  
**Kind**: struct

Constants that represent options you use to fetch a list of user accounts.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
struct QueryOptions
```

## Topics

### Query options
- [static var allDevices: VSUserAccountManager.QueryOptions](vsuseraccountmanager/queryoptions/alldevices.md)
  A constant that indicates fetching user accounts from all the user’s iCloud devices.
### Initializing query options
- [init(rawValue: Int)](vsuseraccountmanager/queryoptions/init(rawvalue:).md)
  Creates a query option from an integer value you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func userAccounts(options: VSUserAccountManager.QueryOptions) async throws -> [VSUserAccount]](vsuseraccountmanager/useraccounts(options:).md)
  Returns a list of registered user accounts for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/queryoptions)*