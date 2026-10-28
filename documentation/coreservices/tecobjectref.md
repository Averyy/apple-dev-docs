# TECObjectRef

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines an opaque reference to a converter object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueTECObjectRef *TECObjectRef;
```

## Discussion

When making a text conversion, the Text Encoding Converter requires a reference to a converter object that indicates how to accomplish the conversion. Functions, such as [`TECCreateConverter`](./api-1571815-teccreateconverter.md), that create a converter object return this reference, which you can then pass to other functions when converting text. A converter object reference is defined by the `TECObjectRef` data type. 

The structure of the `OpaqueTECObjectRef` data type is private, and a converter object is not accessible directly. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecobjectref)*