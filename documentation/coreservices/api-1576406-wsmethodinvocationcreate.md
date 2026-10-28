# WSMethodInvocationCreate

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a reference to a method invocation, containing the URL of the service, the operation name, and the protocol.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
WSMethodInvocationRef WSMethodInvocationCreate(CFURLRef url, CFStringRef methodName, CFStringRef protocol);
```

## Return Value

A `WSMethodInvocationRef` object that can be passed to `WSMethodInvocationInvoke` or scheduled with a run loop.

## Discussion

Creates a web services method invocation object. This is the fundamental object used when passing method parameters or settings, callbacks, or custom serializers or deserializers. This object may be executed synchronously using `WSMethodInvocationInvoke` or scheduled on a run loop for asynchronous execution using `WSMethodInvocationScheduleWithRunLoop`.

## Parameters

- `url`: The endpoint of the service.
- `methodName`: The name of the operation to be called.
- `protocol`: A string defined above that determines the type of invocation object to create. There are string constants for XML-RPC, SOAP 1.1, or SOAP 1.2. Other protocols are not recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576406-wsmethodinvocationcreate)*