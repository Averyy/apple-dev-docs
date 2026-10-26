# Descriptor Type Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify types for descriptors.

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
- [typeAEList](./api-1542788-descriptor_type_constants/typeaelist.md)
  List of descriptors.
- [typeAERecord](./api-1542788-descriptor_type_constants/typeaerecord.md)
  List of keyword-specified descriptors.
- [typeAppleEvent](./api-1542788-descriptor_type_constants/typeappleevent.md)
  Apple event.
- [typeTrue](./api-1542788-descriptor_type_constants/typetrue.md)
  `TRUE` Boolean value.
- [typeFalse](./api-1542788-descriptor_type_constants/typefalse.md)
  `FALSE` Boolean value.
- [typeAlias](./api-1542788-descriptor_type_constants/typealias.md)
  Alias.
- [typeEnumerated](./api-1542788-descriptor_type_constants/typeenumerated.md)
  Enumerated data.
- [typeType](./api-1542788-descriptor_type_constants/typetype.md)
  Four-character code for event class or event ID
- [typeAppParameters](./api-1542788-descriptor_type_constants/typeappparameters.md)
  Process Manager launch parameters.
- [typeProperty](./api-1542788-descriptor_type_constants/typeproperty.md)
  Apple event object property.
- [typeFSRef](./api-1542788-descriptor_type_constants/typefsref.md)
  File system reference. Use in preference to file system specifications (`typeFSS`).
- [typeFileURL](./api-1542788-descriptor_type_constants/typefileurl.md)
  A file URL. That is, the associated data consists of the bytes of a UTF-8 encoded URL with a scheme of "file". This type is appropriate for describing a file that may not yet exist—see [Technical Note 2022](http://developer.apple.com/technotes/tn/tn2022.html) for more information.
- [typeKeyword](./api-1542788-descriptor_type_constants/typekeyword.md)
  Apple event keyword.
- [typeSectionH](./api-1542788-descriptor_type_constants/typesectionh.md)
  Handle to a section record. (Deprecated.)
- [typeWildCard](./api-1542788-descriptor_type_constants/typewildcard.md)
  Matches any type.
- [typeApplSignature](./api-1542788-descriptor_type_constants/typeapplsignature.md)
  Application signature.
- [typeProcessSerialNumber](./api-1542788-descriptor_type_constants/typeprocessserialnumber.md)
  A process serial number. See also [`AEAddressDesc`](./aeaddressdesc.md).
- [typeApplicationURL](./api-1542788-descriptor_type_constants/typeapplicationurl.md)
  For specifying an application by URL. See Discussion section below for important information.
- [typeNull](./api-1542788-descriptor_type_constants/typenull.md)
  A null data storage pointer. When resolving an object specifier, an object with a null storage pointer specifies the default container at the top of the container hierarchy.
- [typeBookmarkData](./api-1542788-descriptor_type_constants/typebookmarkdata.md)
- [typeEventRecord](./api-1542788-descriptor_type_constants/typeeventrecord.md)
- [typeFixed](./api-1542788-descriptor_type_constants/typefixed.md)
- [typeQDRectangle](./api-1542788-descriptor_type_constants/typeqdrectangle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542788-descriptor_type_constants)*