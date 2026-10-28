# WSMethodInvocationGetTypeID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the type ID of the current method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
CFTypeID WSMethodInvocationGetTypeID(void);
```

## Return Value

A CFTypeID.

## Discussion

Returns the ID of the current method invocation. You should call this immediately after creating the invocation reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576434-wsmethodinvocationgettypeid)*