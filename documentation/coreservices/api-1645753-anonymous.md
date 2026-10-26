# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : DescType {
    ...
};
```

## Topics

### Constants
- [typeAbsoluteOrdinal](./api-1645753-anonymous/typeabsoluteordinal.md)
  Specifies a descriptor whose data consists of one of the constants `kAEFirst`, `kAEMiddle`, `kAELast`, `kAEAny`, or `kAEAll`, which are described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md). Used with `formAbsolutePosition`.
- [typeCompDescriptor](./api-1645753-anonymous/typecompdescriptor.md)
  Specifies a comparison descriptor. Data is one of the constants described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md).
- [typeCurrentContainer](./api-1645753-anonymous/typecurrentcontainer.md)
  Specifies a container for an element that demarcates one boundary in a range. The descriptor has a null data storage pointer. This descriptor type is used only with `formRange`.
- [typeIndexDescriptor](./api-1645753-anonymous/typeindexdescriptor.md)
  Specifies a descriptor whose data indicates an indexed position within a range of values.
- [typeLogicalDescriptor](./api-1645753-anonymous/typelogicaldescriptor.md)
  Specifies a logical descriptor. Data is one of the constants described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md).
- [typeOSLTokenList](./api-1645753-anonymous/typeosltokenlist.md)
  Specifies a descriptor whose data consists of a list of tokens. (Token is defined in [`AEDisposeToken`](./api-1446783-aedisposetoken.md).)
- [typeObjectBeingExamined](./api-1645753-anonymous/typeobjectbeingexamined.md)
- [typeObjectSpecifier](./api-1645753-anonymous/typeobjectspecifier.md)
  Specifies a descriptor used with the `keyAEContainer` keyword in a keyword-specified descriptor. The key data for the descriptor is an object specifier.
- [typeRangeDescriptor](./api-1645753-anonymous/typerangedescriptor.md)
- [typeRelativeDescriptor](./api-1645753-anonymous/typerelativedescriptor.md)
  Specifies a descriptor whose data consists of one of the constants `kAENext` or `kAEPrevious`, which are described in [`AEDisposeToken`](./api-1446783-aedisposetoken.md). Used with `formRelativePosition`.
- [typeToken](./api-1645753-anonymous/typetoken.md)
  Specifies a descriptor whose data storage pointer refers to a structure of type [`AEDisposeToken`](./api-1446783-aedisposetoken.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1645753-anonymous)*