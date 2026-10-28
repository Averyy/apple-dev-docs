# TECSnifferObjectRef

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a reference to an opaque sniffer object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueTECSnifferObjectRef *TECSnifferObjectRef;
```

## Discussion

When analyzing text for possible encodings, the Text Encoding Converter requires a reference to a sniffer object that specifies what types of encodings can be detected. You receive this reference when calling the function [`TECCreateSniffer`](./api-1571832-teccreatesniffer.md). A sniffer object reference is defined by the `TECSnifferObjectRef` data type. The structure of the `OpaqueTECObjectRef` data type is private, and a sniffer object is not accessible directly. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecsnifferobjectref)*