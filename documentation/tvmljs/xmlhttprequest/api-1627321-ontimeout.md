# ontimeout

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function that is called when a request times out.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute function ontimeout;
```

#### Discussion

This attribute must be set to a function; for example, `XMLHttpRequest.ontimeout = function () {}`.

## See Also

- [onabort](xmlhttprequest/1627410-onabort.md)
  A callback function called when a request is cancelled by the user.
- [onerror](xmlhttprequest/1627328-onerror.md)
  A callback function that is called if the request fails due to an error.
- [onload](xmlhttprequest/1627316-onload.md)
  A callback function that is called when the request is successfully completed.
- [onloadend](xmlhttprequest/1627365-onloadend.md)
  A callback function that is called when the request is completed for any reason.
- [onloadstart](xmlhttprequest/1627440-onloadstart.md)
  A callback function that is called when the request begins.
- [onreadystatechange](xmlhttprequest/1627414-onreadystatechange.md)
  A callback function that is called when the [`readyState`](xmlhttprequest/1627324-readystate.md) attribute changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627321-ontimeout)*