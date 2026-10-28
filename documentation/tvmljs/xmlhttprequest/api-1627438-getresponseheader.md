# getResponseHeader

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Retrieves the field value from the response that is contained in the specified header.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

*tvOS*

```
String getResponseHeader(
    in String header
);
```

*Safari Desktop, Safari Mobile*

```
DOMString? getResponseHeader(
    DOMString header
);
```

## Return Value

The header field value.

## Discussion

If the header value is `Set-Cookie` or `Set-Cookie2`, the value inside the header will not be returned. This method returns `null` if no response has been received or if the specified header doesn’t exist.

## Parameters

- `header`: The header field name. An exception is raised if this value is not `null` or `String`.

## See Also

### Manipulating the Header List
- [getAllResponseHeaders](./api-1627343-getallresponseheaders.md)
  Returns all of the response headers.
- [setRequestHeader](./api-1627317-setrequestheader.md)
  Appends a header to the list of request headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627438-getresponseheader)*