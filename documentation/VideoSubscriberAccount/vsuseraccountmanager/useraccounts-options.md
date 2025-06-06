# userAccounts(options:)

**Framework**: Videosubscriberaccount  
**Kind**: method

Returns a list of registered user accounts for your app.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+

## Declaration

```swift
func userAccounts(options: VSUserAccountManager.QueryOptions = []) async throws -> [VSUserAccount]
```

#### Return Value

A list of registered user accounts for your app.

#### Discussion

By default, this fetches and returns the list of registered user accounts on the current device. Provide the query option [`allDevices`](vsuseraccountmanager/queryoptions/alldevices.md) to fetch the list of registered user accounts on all the devices the user has in their iCloud account.

## Parameters

- `options`: An array of options you specify to customize the user account query.

## See Also

- [VSUserAccountManager.QueryOptions](vsuseraccountmanager/queryoptions.md)
  Constants that represent options you use to fetch a list of user accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/useraccounts(options:))*