# status

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The HTTP status code.

**Availability**:
- tvOS 9.0+
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

*tvOS*

```
readonly attribute int status;
```

*Safari Desktop, Safari Mobile*

```
readonly attribute unsigned short status;
```

## Discussion

If the current state of the request is `unsent` or `opened`, then this attribute’s value is `0`.

## See Also

### Retrieving Request Information
- [metrics](./api-1627436-metrics.md)
  A dictionary of keys used to request start and response start and end times.
- [readyState](./api-1627324-readystate.md)
  The current state of the request.
- [response](./api-1627364-response.md)
  The response entity body.
- [responseCacheIsValid](../../webkitjs/xmlhttprequest/api-2871089-responsecacheisvalid.md)
- [responseText](./api-1627363-responsetext.md)
  The response to the request.
- [responseType](./api-1627342-responsetype.md)
  The type of response.
- [responseURL](../../webkitjs/xmlhttprequest/api-1630664-responseurl.md)
- [responseXML](./api-1627307-responsexml.md)
  The document response entity body.
- [statusText](./api-1627375-statustext.md)
  The HTTP status text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627403-status)*