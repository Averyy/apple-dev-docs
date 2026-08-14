# VSUserAccountManager.QueryOptions

**Framework**: Video Subscriber Account  
**Kind**: struct

Constants that represent options you use to fetch a list of user accounts.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func userAccounts(options: VSUserAccountManager.QueryOptions) async throws -> [VSUserAccount]](vsuseraccountmanager/useraccounts(options:).md)
  Returns a list of registered user accounts for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/queryoptions)*