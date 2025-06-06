# setRequestHeader

**Framework**: TVMLKit JS  
**Kind**: instm

Appends a header to the list of request headers.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
void setRequestHeader(
    DOMString header, 
    DOMString value
);
```

#### Discussion

If the header already exists in the list of request headers, the specified value is combined with the value currently in the list to create a single request header.

## Parameters

- `header`: The header name.
- `value`: The header value.

## See Also

- [getAllResponseHeaders](xmlhttprequest/1627343-getallresponseheaders.md)
  Returns all of the response headers.
- [getResponseHeader](xmlhttprequest/1627438-getresponseheader.md)
  Retrieves the field value from the response that is contained in the specified header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627317-setrequestheader)*