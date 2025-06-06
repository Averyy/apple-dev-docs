# TVError

**Framework**: TVMLKit JS  
**Kind**: cl

Error codes for the TVError domain.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
interface TVError
```

#### Overview

A `TVError` object encapsulates richer and more extensible error information than is possible when you use only an error code or error string. The core attributes of a `TVError` object are an error domain (represented by a string), a domain-specific error code, and a user info dictionary containing app-specific information. See [`User Info Dictionary Keys`](tverror/user_info_dictionary_keys.md) and [`Error Domains`](tverror/error_domains.md).

## Topics

### Getting Error Properties
- [code](tverror/1627334-code.md)
  The error code.
- [description](tverror/1627424-description.md)
  A string containing the description of the error.
- [domain](tverror/1627426-domain.md)
  A string containing the error domain.
- [userInfo](tverror/1627388-userinfo.md)
  The user info dictionary.
### Constants
- [User Info Dictionary Keys](tverror/user_info_dictionary_keys.md)
  Keys that exist in the user info dictionary.
- [Error Domains](tverror/error_domains.md)
  The predefined error domains.

## See Also

- [NSError](nserror.md)
  Information about an error condition, including a domain, a domain-specific error code, and application-specific information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/tverror)*