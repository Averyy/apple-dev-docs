# WSMethodInvocationSerializationProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is an optional callback that handles custom serialization of a particular data type for method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
typedef CFStringRef (*WSMethodInvocationSerializationProcPtr)(WSMethodInvocationRef invocation, CFTypeRef obj, void *info);
```

## Return Value

A `CFStringRef` containing valid XML.  The caller of this callback will release the string. If you return `NULL`, the default serializer is used.

## Discussion

If your callback is named MySerilaizerCallback, declare it like this:

### Discussion

This callback is called whenever a type to be serialized by the method invocation has the given CFTypeID. The callback should return an XML snippet that will be understood by the server as a correct serialization for a given type.  If the callback returns `NULL`, the default serializer is used.

## Parameters

- `invocation`: The method invocation for which this callback handles serialization.
- `obj`: The CFTypeRef for which this callback produces serialized XML.
- `info`: Private callback data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsmethodinvocationserializationprocptr)*