# WSMethodInvocationSetCallBack

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Set a callback to handle the response to an asynchronous method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationSetCallBack(WSMethodInvocationRef invocation, WSMethodInvocationCallBackProcPtr clientCB, WSClientContext *context);
```

## Discussion

Sets the callback to handle the response for an asynchronous method invocation.  The callback is passed a reference to the method invocation just completed, a pointer to private data, and a dictionary that contains the return values for the operation or a fault structure. Test for a fault using `WSMethodResultIsFault`. The callback parses the method response dictionary, which contains the deserialized return data, and may contain the raw XML of the return message as well. The callback is responsible for releasing the result ref. 

Call with a `clientCB` and context of `NULL` to clear the invocation callback.

## Parameters

- `invocation`: The method invocation reference.
- `clientCB`: A `ProcPtr` to be called when the invocation completes.
- `context`: A pointer to a `WSClientContext`. The structure will be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576439-wsmethodinvocationsetcallback)*