# WSProtocolHandlerSerializationProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is an optional callback that handles custom serialization of a particular data type for a protocol handler.

**Availability**:
- macOS 10.3+

## Declaration

```c
typedef CFStringRef (*WSProtocolHandlerSerializationProcPtr)(WSProtocolHandlerRef protocol, CFTypeRef obj, void *info);
```

## Return Value

A `CFStringRef` containing valid XML.  The caller of this callback will release the string. If you return `NULL`, the default serializer is used.

## Discussion

If your callback is named MySerilaizerCallback, declare it like this:

### Discussion

This callback is called whenever a type to be serialized by the protocol handler has the given CFTypeID. The callback should return an XML snippet that will be understood by the server as a correct serialization for a given type.  If the callback returns `NULL`, the default serializer is used.

> ❗ **Important**: For SOAP serializations, the parameter key (element name) is not part of the callback; it will be substituded for all occurances of "%@" in the returned string.

## Parameters

- `protocol`: The protocol handler for which this callback handles serialization.
- `obj`: The CFTypeRef for which this callback produces serialized XML.
- `info`: Private callback data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsprotocolhandlerserializationprocptr)*