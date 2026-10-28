# WSMethodInvocationAddSerializationOverride

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Specifies a callback to be made when creating the XML for an method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationAddSerializationOverride(WSMethodInvocationRef invocation, CFTypeID objType, WSMethodInvocationSerializationProcPtr serializationProc, WSClientContext *context);
```

## Discussion

Specifies a callback which will be called to produce the XML that represents the serialization of a given type ref.  See `WSTypes.h` for a list of `CFTypes` for which there are default serializers.  If your callback returns `NULL`, the default serializer will be used.

## Parameters

- `invocation`: The invocation currently being serialized
- `objType`: The `CFTypeID` of the object to serialize
- `serializationProc`: The `ProcPtr` to the callback
- `context`:  A pointer to a `WSClientContext`.  The structure will be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576435-wsmethodinvocationaddserializati)*