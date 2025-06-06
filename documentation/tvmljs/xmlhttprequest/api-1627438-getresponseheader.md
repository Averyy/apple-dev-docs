# getResponseHeader

**Framework**: TVMLKit JS  
**Kind**: instm

Retrieves the field value from the response that is contained in the specified header.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
DOMString? getResponseHeader(
    DOMString header
);
```

#### Return_value

The header field value.

#### Discussion

If the header value is `Set-Cookie` or `Set-Cookie2`, the value inside the header will not be returned. This method returns `null` if no response has been received or if the specified header doesn’t exist.

## Parameters

- `header`: The header field name. An exception is raised if this value is not   or  .

## See Also

- [getAllResponseHeaders](xmlhttprequest/1627343-getallresponseheaders.md)
  Returns all of the response headers.
- [setRequestHeader](xmlhttprequest/1627317-setrequestheader.md)
  Appends a header to the list of request headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627438-getresponseheader)*