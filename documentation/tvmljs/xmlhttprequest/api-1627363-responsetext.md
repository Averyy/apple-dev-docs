# responseText

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The response to the request.

**Availability**:
- tvOS 9.0+
- Safari Desktop 9.0+
- Safari Mobile 9.0+

## Declaration

*tvOS*

```
readonly attribute String responseText;
```

*Safari Desktop, Safari Mobile*

```
readonly attribute DOMString? responseText;
```

#### Discussion

If the request was unsuccessful or has not been sent, the value of this attribute is `null`. Otherwise, this attribute contains a string containing the response.

## See Also

### Retrieving Request Information
- [metrics](./api-1627436-metrics.md)
  A dictionary of keys used to request start and response start and end times.
- [readyState](./api-1627324-readystate.md)
  The current state of the request.
- [response](./api-1627364-response.md)
  The response entity body.
- [responseCacheIsValid](../../webkitjs/xmlhttprequest/api-2871089-responsecacheisvalid.md)
- [responseType](./api-1627342-responsetype.md)
  The type of response.
- [responseURL](../../webkitjs/xmlhttprequest/api-1630664-responseurl.md)
- [responseXML](./api-1627307-responsexml.md)
  The document response entity body.
- [status](./api-1627403-status.md)
  The HTTP status code.
- [statusText](./api-1627375-statustext.md)
  The HTTP status text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627363-responsetext)*