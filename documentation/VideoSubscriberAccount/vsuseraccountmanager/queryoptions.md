# VSUserAccountManager.QueryOptions

**Framework**: Video Subscriber Account  
**Kind**: struct  
**Role**: Structure

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

```c
enum VSUserAccountQueryOptions : NSInteger;
```

## Topics

### Query options
- [static var allDevices: VSUserAccountManager.QueryOptions](./queryoptions/alldevices.md)
  A constant that indicates fetching user accounts from all the user’s iCloud devices.
### Initializing query options
- [init(rawValue: Int)](./queryoptions/init%28rawvalue%29.md)
  Creates a query option from an integer value you provide.
- [VSUserAccountQueryNone](../vsuseraccountqueryoptions/vsuseraccountquerynone.md)
  A constant that indicates fetching user accounts from the user’s current device only.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting user accounts
- [func userAccounts(options: VSUserAccountManager.QueryOptions) async throws -> [VSUserAccount]](./useraccounts%28options%29.md)
  Returns a list of registered user accounts for your app.
- [- queryUserAccountsWithOptions:completion:](./queryuseraccountswithoptions_completion_.md)
  Returns a list of registered user accounts for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/queryoptions)*