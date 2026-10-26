# WSMethodInvocationAddDeserializationOverride

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Specifies a callback to be made when parsing the XML in a method response.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationAddDeserializationOverride(WSMethodInvocationRef invocation, CFStringRef typeNamespace, CFStringRef typeName, WSMethodInvocationDeserializationProcPtr deserializationProc, WSClientContext *context);
```

#### Discussion

Specifies a callback to be made when parsing an XML method response.  Used to deserialize types the default deserializer does not handle. The callback should return a `CFTypeRef` containing the deserialized object value.  If the callback returns `NULL`, the default deserializer is used.

## Parameters

- `invocation`: The method invocation reference.
- `typeNamespace`: The fully resolved namespace for a specific type. For example, this field could be: `CFSTR("http://www.Myserver.com/myNameSpace")`. If `NULL`, the default namespace will be used.
- `typeName`: The non-qualified type name. Note that this is the XML /name/ to be deserialized, not the name of the type. For example, if the XML is  `<Sharename xsi:type="xsd:string">Album-9</Sharename>`, the `typeName` is `Sharename`, not `string`. This parameter must not be `NULL`.
- `deserializationProc`: A `ProcPtr` to the callback to be called to perform the deserialization.
- `context`: A pointer to a `WSClientContext`. The structure will be copied.

## See Also

### Related Documentation
- [Web Services Core Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/UsingWebservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP30000985)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576436-wsmethodinvocationadddeserializa)*