# responseType

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The type of response.

**Availability**:
- tvOS 9.0+
- Safari Desktop 5.1+
- Safari Mobile 5.0+

## Declaration

*tvOS*

```
attribute String responseType;
```

*Safari Desktop, Safari Mobile*

```
attribute XMLHttpRequestResponseType responseType;
```

## Discussion

Valid values for this attribute are the empty string, `blob`, `document`, `json,` and `text`.

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
- [responseURL](../../webkitjs/xmlhttprequest/api-1630664-responseurl.md)
- [responseXML](./api-1627307-responsexml.md)
  The document response entity body.
- [status](./api-1627403-status.md)
  The HTTP status code.
- [statusText](./api-1627375-statustext.md)
  The HTTP status text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627342-responsetype)*