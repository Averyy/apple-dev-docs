# readyState

**Framework**: TVMLKit JS  
**Kind**: instp

The current state of the request.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
readonly attribute unsigned short readyState;
```

#### Discussion

This attribute can have the following values:

- `0 - UNSENT`
- `1 - OPENED`
- `2 - HEADERS_RECEIVED`
- `3 - LOADING`
- `4 - DONE`

## See Also

- [metrics](xmlhttprequest/1627436-metrics.md)
  A dictionary of keys used to request start and response start and end times.
- [response](xmlhttprequest/1627364-response.md)
  The response entity body.
- [responseCacheIsValid](../webkitjs/xmlhttprequest/2871089-responsecacheisvalid.md)
- [responseText](xmlhttprequest/1627363-responsetext.md)
  The response to the request.
- [responseType](xmlhttprequest/1627342-responsetype.md)
  The type of response.
- [responseURL](../webkitjs/xmlhttprequest/1630664-responseurl.md)
- [responseXML](xmlhttprequest/1627307-responsexml.md)
  The document response entity body.
- [status](xmlhttprequest/1627403-status.md)
  The HTTP status code.
- [statusText](xmlhttprequest/1627375-statustext.md)
  The HTTP status text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627324-readystate)*