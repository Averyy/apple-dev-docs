# abort

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Cancels any network activity.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```
void abort();
```

## Discussion

This method raises a `DOMException` if any arguments are passed into this function.

## See Also

### Initializing and Sending a Request
- [open](./api-1627318-open.md)
  Sets the method, URL, and synchronous flag for a request.
- [send](./api-1627309-send.md)
  Sends the request.
- [timeout](./api-1627335-timeout.md)
  The amount of time, in milliseconds, before causing a request to time out.
- [XMLHttpRequest](./api-1627350-xmlhttprequest.md)
  Creates a new XMLHttpRequest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627356-abort)*