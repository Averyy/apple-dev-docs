# Common and Special Unicode Values

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify sommon and special Unicode code values.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kUnicodeByteOrderMark](./api-1400154-common_and_special_unicode_value/kunicodebyteordermark.md)
- [kUnicodeObjectReplacement](./api-1400154-common_and_special_unicode_value/kunicodeobjectreplacement.md)
  A placeholder for a non-text object.
- [kUnicodeReplacementChar](./api-1400154-common_and_special_unicode_value/kunicodereplacementchar.md)
  Unicode replacement for an input character that cannot be converted.
- [kUnicodeSwappedByteOrderMark](./api-1400154-common_and_special_unicode_value/kunicodeswappedbyteordermark.md)
  Not a Unicode character; byte-swapped version of FEFF.
- [kUnicodeNotAChar](./api-1400154-common_and_special_unicode_value/kunicodenotachar.md)
  Not a Unicode character; may be used as a terminator.

## See Also

### Assorted Constants
- [Bidirectional Character Values](./api-1400035-bidirectional_character_values.md)
  Specify bidirectional character properties.
- [TEC Plugin Dispatch Table Versions](./api-1498348-tec_plugin_dispatch_table_versio.md)
  Specify a version for a TEC plug-in dispatch table.
- [TEC Plug-in Signatures](./api-1571831-tec_plug-in_signatures.md)
  Specify a TEC plug-in signature.
- [UCCharPropertyType](./uccharpropertytype.md)
  Specify property types for a Unicode charater.
- [UCCharPropertyValue](./uccharpropertyvalue.md)
  Specify a propery value for a Unicode character.
- [UnicodeMapVersion](./unicodemapversion.md)
  Specify a Unicode mapping version.
- [Unwanted Data Constants](./api-1400314-unwanted_data_constants.md)
  Specify data you don’t care about receiving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400154-common_and_special_unicode_value)*