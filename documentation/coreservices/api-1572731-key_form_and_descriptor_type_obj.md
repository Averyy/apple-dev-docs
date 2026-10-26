# Key Form and Descriptor Type Object Specifier Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify possible values for the `keyAEKeyForm` field of an object specifier, as well as descriptor types used in resolving object specifiers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [formAbsolutePosition](./api-1572731-key_form_and_descriptor_type_obj/formabsoluteposition.md)
- [formRelativePosition](./api-1572731-key_form_and_descriptor_type_obj/formrelativeposition.md)
- [formTest](./api-1572731-key_form_and_descriptor_type_obj/formtest.md)
- [formRange](./api-1572731-key_form_and_descriptor_type_obj/formrange.md)
- [formPropertyID](./api-1572731-key_form_and_descriptor_type_obj/formpropertyid.md)
  Specifies the property ID for an element’s property.
- [formName](./api-1572731-key_form_and_descriptor_type_obj/formname.md)
  Specifies the Apple event object by name.
- [typeObjectSpecifier](./api-1645753-anonymous/typeobjectspecifier.md)
  Specifies a descriptor used with the `keyAEContainer` keyword in a keyword-specified descriptor. The key data for the descriptor is an object specifier.
- [typeObjectBeingExamined](./api-1645753-anonymous/typeobjectbeingexamined.md)
- [typeCurrentContainer](./api-1645753-anonymous/typecurrentcontainer.md)
  Specifies a container for an element that demarcates one boundary in a range. The descriptor has a null data storage pointer. This descriptor type is used only with `formRange`.
- [typeToken](./api-1645753-anonymous/typetoken.md)
  Specifies a descriptor whose data storage pointer refers to a structure of type [`AEDisposeToken`](./api-1446783-aedisposetoken.md).
- [typeRelativeDescriptor](./api-1645753-anonymous/typerelativedescriptor.md)
  Specifies a descriptor whose data consists of one of the constants `kAENext` or `kAEPrevious`, which are described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md). Used with `formRelativePosition`.
- [typeAbsoluteOrdinal](./api-1645753-anonymous/typeabsoluteordinal.md)
  Specifies a descriptor whose data consists of one of the constants `kAEFirst`, `kAEMiddle`, `kAELast`, `kAEAny`, or `kAEAll`, which are described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md). Used with `formAbsolutePosition`.
- [typeIndexDescriptor](./api-1645753-anonymous/typeindexdescriptor.md)
  Specifies a descriptor whose data indicates an indexed position within a range of values.
- [typeRangeDescriptor](./api-1645753-anonymous/typerangedescriptor.md)
- [typeLogicalDescriptor](./api-1645753-anonymous/typelogicaldescriptor.md)
  Specifies a logical descriptor. Data is one of the constants described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md).
- [typeCompDescriptor](./api-1645753-anonymous/typecompdescriptor.md)
  Specifies a comparison descriptor. Data is one of the constants described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md).
- [typeOSLTokenList](./api-1645753-anonymous/typeosltokenlist.md)
  Specifies a descriptor whose data consists of a list of tokens. (Token is defined in [`AEDisposeToken`](./api-1446783-aedisposetoken.md).)
- [formUniqueID](./api-1572731-key_form_and_descriptor_type_obj/formuniqueid.md)
  Specifies a value that uniquely identifies an object within its container or across an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1572731-key_form_and_descriptor_type_obj)*