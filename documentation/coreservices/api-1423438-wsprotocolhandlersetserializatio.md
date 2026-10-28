# WSProtocolHandlerSetSerializationOverride

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Specifies a callback which will be called to produce the XML that represents the serialization of a given type ref.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
void WSProtocolHandlerSetSerializationOverride(WSProtocolHandlerRef protocol, CFTypeID objType, WSProtocolHandlerSerializationProcPtr serializationProc, WSClientContext *context);
```

## Discussion

This function specifies a callback which will be called to produce the XML that represents the serialization of a given type ref. This callback is called whenever a type has the given `CFTypeID`. The callback should return an XML snippet that will be understood by the server as a correct serialization for a given type.  If the callback returns NULL, the default serializer is used. For SOAP serializations, the parameter key (element name) is not part of the callback; it will be substituded for all occurances of "%@" in the returned string. If your callback returns `NULL`, the default serializer will be used.

## Parameters

- `protocol`: The protocol which is to be executed.
- `objType`: The `CFTypeID` of the object to be serialized.
- `serializationProc`: The serialization callback that will do the work.
- `context`: A pointer to a `WSClientContext`. The structure will be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1423438-wsprotocolhandlersetserializatio)*