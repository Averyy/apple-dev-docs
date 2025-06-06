# VSUserAccountManager

**Framework**: Videosubscriberaccount  
**Kind**: class

The object that coordinates your app’s user account actions.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
class VSUserAccountManager
```

#### Overview

Don’t create `VSUserAccountManager` directly; use [`shared`](vsuseraccountmanager/shared.md).

## Topics

### Getting the account manager
- [class var shared: VSUserAccountManager](vsuseraccountmanager/shared.md)
  A shared instance of the user account manager class.
### Getting user accounts
- [func userAccounts(options: VSUserAccountManager.QueryOptions) async throws -> [VSUserAccount]](vsuseraccountmanager/useraccounts(options:).md)
  Returns a list of registered user accounts for your app.
- [VSUserAccountManager.QueryOptions](vsuseraccountmanager/queryoptions.md)
  Constants that represent options you use to fetch a list of user accounts.
### Updating a user account
- [func update(VSUserAccount) async throws](vsuseraccountmanager/update(_:).md)
  Registers a new user account.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct VSUserAccount](vsuseraccount-swift.struct.md)
  An object that represents a user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager)*