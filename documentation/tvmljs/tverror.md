# TVError

**Framework**: TVMLKit JS  
**Kind**: cl  
**Role**: Class

Error codes for the TVError domain.

**Availability**:
- tvOS 9.0+

## Declaration

```
interface TVError
```

#### Overview

A `TVError` object encapsulates richer and more extensible error information than is possible when you use only an error code or error string. The core attributes of a `TVError` object are an error domain (represented by a string), a domain-specific error code, and a user info dictionary containing app-specific information. See [User Info Dictionary Keys](./tverror/user_info_dictionary_keys.md) and [Error Domains](./tverror/error_domains.md).

## Topics

### Getting Error Properties
- [code](./tverror/api-1627334-code.md)
  The error code.
- [description](./tverror/api-1627424-description.md)
  A string containing the description of the error.
- [domain](./tverror/api-1627426-domain.md)
  A string containing the error domain.
- [userInfo](./tverror/api-1627388-userinfo.md)
  The user info dictionary.
### Constants
- [User Info Dictionary Keys](./tverror/user_info_dictionary_keys.md)
  Keys that exist in the user info dictionary.
- [Error Domains](./tverror/error_domains.md)
  The predefined error domains.

## See Also

### Errors
- [NSError](./nserror.md)
  Information about an error condition, including a domain, a domain-specific error code, and application-specific information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/tverror)*