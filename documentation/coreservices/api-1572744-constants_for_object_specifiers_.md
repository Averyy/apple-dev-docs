# Constants for Object Specifiers, Positions, and Logical and Comparison Operations

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify the types of the four keyword-specified descriptors that make up the data in an object specifier, as well as constants for position, logical operations, and comparison operations.

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
- [kAEAND](./api-1572744-constants_for_object_specifiers_/kaeand.md)
  Specifies a logical `AND` operation.
- [kAEOR](./api-1572744-constants_for_object_specifiers_/kaeor.md)
  Specifies a logical `OR` operation.
- [kAENOT](./api-1572744-constants_for_object_specifiers_/kaenot.md)
  Specifies a logical `NOT` operation.
- [kAEFirst](./api-1572744-constants_for_object_specifiers_/kaefirst.md)
  The first element in the specified container.
- [kAELast](./api-1572744-constants_for_object_specifiers_/kaelast.md)
  Specifies the last element in the container.
- [kAEMiddle](./api-1572744-constants_for_object_specifiers_/kaemiddle.md)
- [kAEAny](./api-1572744-constants_for_object_specifiers_/kaeany.md)
  Specifies a single element chosen at random from the container.
- [kAEAll](./api-1572744-constants_for_object_specifiers_/kaeall.md)
  Specifies all the elements in the container.
- [kAENext](./api-1572744-constants_for_object_specifiers_/kaenext.md)
  Specifies the Apple event object after the container.
- [kAEPrevious](./api-1572744-constants_for_object_specifiers_/kaeprevious.md)
  Specifies the Apple event object before the container.
- [keyAECompOperator](./api-1572744-constants_for_object_specifiers_/keyaecompoperator.md)
  Specifies a descriptor of `typeType`, whose data consists of one of the constant values described in [Key Form and Descriptor Type Object Specifier Constants](./api-1572731-key_form_and_descriptor_type_obj.md).
- [keyAELogicalTerms](./api-1572744-constants_for_object_specifiers_/keyaelogicalterms.md)
  Specifies a descriptor of type `typeAEList` containing one or more comparison or logical descriptors.
- [keyAELogicalOperator](./api-1572744-constants_for_object_specifiers_/keyaelogicaloperator.md)
  Specifies a descriptor of type `typeEnumerated` whose data is one of the logical operators (such as `kAEAND`) defined in [Key Form and Descriptor Type Object Specifier Constants](./api-1572731-key_form_and_descriptor_type_obj.md).
- [keyAEObject1](./api-1572744-constants_for_object_specifiers_/keyaeobject1.md)
- [keyAEObject2](./api-1572744-constants_for_object_specifiers_/keyaeobject2.md)
- [keyAEDesiredClass](./api-1572744-constants_for_object_specifiers_/keyaedesiredclass.md)
- [keyAEContainer](./api-1572744-constants_for_object_specifiers_/keyaecontainer.md)
  Specifies the container for the requested object or objects. The data is an object specifier (or in some cases a null descriptor).
- [keyAEKeyForm](./api-1572744-constants_for_object_specifiers_/keyaekeyform.md)
- [keyAEKeyData](./api-1572744-constants_for_object_specifiers_/keyaekeydata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1572744-constants_for_object_specifiers_)*