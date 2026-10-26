# getSecureBootEnabled:error:

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether Secure Boot is in an enabled state in the variable store.

**Availability**:
- macOS 27.0+

## Declaration

```objc
- (BOOL) getSecureBootEnabled:(BOOL *) enabled error:(NSError **) error;
```

#### Return Value

`YES` if the operation succeeded, `NO` if an error occurred.

## Parameters

- `enabled`: On success, set to YES if Secure Boot is enabled, NO otherwise.
- `error`: Assigned with the error if the operation fails, or `nil` upon success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/getsecurebootenabled:error:)*