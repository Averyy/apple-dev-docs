# NSError

**Framework**: TVMLKit JS  
**Kind**: cl  
**Role**: Class

Information about an error condition, including a domain, a domain-specific error code, and application-specific information.

**Availability**:
- tvOS 11.0+

## Declaration

```
interface NSError
```

## Topics

### Getting Error Properties
- [code](./nserror/api-2897820-code.md)
  The error code.
- [domain](./nserror/api-2897831-domain.md)
  A string containing the error domain.
- [userInfo](./nserror/api-2897822-userinfo.md)
  The user info dictionary.
- [underlyingError](./nserror/api-2897821-underlyingerror.md)
  The error that was encountered in an underlying implementation and caused the error that the receiver represents to occur.
### Getting a Localized Error Description
- [description](./nserror/api-2897823-description.md)
  A string containing the localized description of the error.
- [failureReason](./nserror/api-2897833-failurereason.md)
  A string containing the localized explanation of the reason for the error.
- [recoverySuggestion](./nserror/api-2897824-recoverysuggestion.md)
  A string containing the localized recovery suggestion for the error.

## See Also

### Errors
- [TVError](./tverror.md)
  Error codes for the TVError domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/nserror)*