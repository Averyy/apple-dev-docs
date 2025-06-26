# init(endpoint:targetQueue:options:cancellationHandler:)

**Framework**: XPC  
**Kind**: init

Creates a new session object representing a connection to the xpc endpoint.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@preconcurrency
convenience init(endpoint: XPCEndpoint, targetQueue: DispatchQueue? = nil, options: XPCSession.InitializationOptions = .none, cancellationHandler: ((XPCRichError) -> Void)? = nil) throws
```

#### Return Value

Returns a new session object. The returned session is activated by default and can be used to send messages.

#### Discussion

> **Note**: A `XPCRichError` describing the details of the error that occurred.

This will throw a XPCRichError if the specified endpoint is invalid or unavailable.

## Parameters

- `endpoint`: The endpoint to create a session with.
- `targetQueue`: The GCD queue onto which session events will be submitted.   This may be a concurrent queue. This parameter is optional, if the target queue is   not specified the target queue will be libdispatch’s default target queue, defined as   .
- `options`: Additional attributes which which to create the session.
- `cancellationHandler`: The cancellation handler block that will be executed when this session is cancelled.   This parameter is optional. See 


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/init(endpoint:targetqueue:options:cancellationhandler:))*