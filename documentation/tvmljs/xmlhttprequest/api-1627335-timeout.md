# timeout

**Framework**: TVMLKit JS  
**Kind**: instp

The amount of time, in milliseconds, before causing a request to time out.

**Availability**:
- tvOS 9.0+
- Safari Desktop 9.0+
- Safari Mobile 9.0+

## Declaration

```swift
attribute unsigned long timeout;
```

#### Discussion

This attribute only takes effect if the request is asynchronous. When set to `0`, the request will not automatically time out.

## See Also

- [abort](xmlhttprequest/1627356-abort.md)
  Cancels any network activity.
- [open](xmlhttprequest/1627318-open.md)
  Sets the method, URL, and synchronous flag for a request.
- [send](xmlhttprequest/1627309-send.md)
  Sends the request.
- [XMLHttpRequest](xmlhttprequest/1627350-xmlhttprequest.md)
  Creates a new XMLHttpRequest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xmlhttprequest/1627335-timeout)*