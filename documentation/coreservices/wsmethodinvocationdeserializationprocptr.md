# WSMethodInvocationDeserializationProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

This is an optional callback that handles custom deserialization of a particular data type for a method response.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
typedef CFTypeRef (*WSMethodInvocationDeserializationProcPtr)(WSMethodInvocationRef invocation, CFXMLTreeRef msgRoot, CFXMLTreeRef deserializeRoot, void *info);
```

## Return Value

A `CFTypeRef` representing the deserialized data. The caller will release this data. If you return `NULL`, the default deserializer is used.

## Discussion

If your callback is named MyDeserilaizerCallback, declare it like this:

### Discussion

This callback is passed a reference to the invocation currently being executed, the root of the response parse tree, the current node being deserialized, and a pointer to private data. The return result should be a valid `CFTypeRef` object (which will be released  by the caller) or `NULL` to allow the default deserializer to act. Unlike the serialization callback, which is called only for a specified data type, the deserialization callback is called for every element to be deserialized.

## Parameters

- `invocation`: The method invocation for which this callback handles deserialization.
- `msgRoot`: The root element of the XML to be deserialized.
- `deserializeRoot`: The tree element of the XML to be deserialized.
- `info`: Private callback data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/wsmethodinvocationdeserializationprocptr)*