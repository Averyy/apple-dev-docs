# WSMethodInvocationRef

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

An opaque reference to a web services method invocation.

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef struct OpaqueWSMethodInvocationRef *WSMethodInvocationRef;
```

#### Discussion

The `WSMethodInvocationRef` is the fundamental object of web services. Create it using `WSMethodInvocationCreate`. Use it to set parameters, callbacks, and settings for a method invocation, and to invoke a method and obtain a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsmethodinvocationref)*