# queryUserAccountsWithOptions:completion:

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Returns a list of registered user accounts for your app.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```objc
- (void) queryUserAccountsWithOptions:(VSUserAccountQueryOptions) options completion:(void (^)(NSArray<VSUserAccount *> *accounts, NSError *error)) completion;
```

## Discussion

By default, this fetches and returns the list of registered user accounts on the current device. Provide the query option [`allDevices`](./queryoptions/alldevices.md) to fetch the list of registered user accounts on all the devices the person has in their iCloud account.

## Parameters

- `options`: An array of options you specify to customize the user account query.
- `completion`: The closure that the user account manager executes after the request completes. This closure has no return value and takes the following parameters:

  - **accounts**: A list of registered user accounts for your app.
  - **error**: An error object that contains information about a problem, or `nil` if the request completed successfully.

## See Also

### Getting user accounts
- [VSUserAccountManager.QueryOptions](./queryoptions.md)
  Constants that represent options you use to fetch a list of user accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/queryuseraccountswithoptions:completion:)*