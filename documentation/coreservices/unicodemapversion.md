# UnicodeMapVersion

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Specify a Unicode mapping version.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef SInt32 UnicodeMapVersion;
```

## Discussion

When performing conversions, you specify the version of the Unicode mapping table to be used for the conversion. You provide the version number in the mapping version field of the structure [`UnicodeMapping`](./unicodemapping.md) that is passed to a function. A Unicode mapping version is defined by the `UnicodeMapVersion` data type.  

## Topics

### Constants
- [kUnicodeUseLatestMapping](./api-1433552-anonymous/kunicodeuselatestmapping.md)
  Instead of explicitly specifying the mapping version of the Unicode mapping table to be used for conversion of a text string, you can use this constant to specify that the latest version be used. 
- [kUnicodeUseHFSPlusMapping](./api-1433552-anonymous/kunicodeusehfsplusmapping.md)
  Indicates the mapping version used by HFS Plus to convert filenames between Mac OS encodings and Unicode. Only one constant is defined so far for a specific mapping version. 

## See Also

### Assorted Constants
- [Bidirectional Character Values](./api-1400035-bidirectional_character_values.md)
  Specify bidirectional character properties.
- [Common and Special Unicode Values](./api-1400154-common_and_special_unicode_value.md)
  Specify sommon and special Unicode code values.
- [TEC Plugin Dispatch Table Versions](./api-1498348-tec_plugin_dispatch_table_versio.md)
  Specify a version for a TEC plug-in dispatch table.
- [TEC Plug-in Signatures](./api-1571831-tec_plug-in_signatures.md)
  Specify a TEC plug-in signature.
- [UCCharPropertyType](./uccharpropertytype.md)
  Specify property types for a Unicode charater.
- [UCCharPropertyValue](./uccharpropertyvalue.md)
  Specify a propery value for a Unicode character.
- [Unwanted Data Constants](./api-1400314-unwanted_data_constants.md)
  Specify data you don’t care about receiving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/unicodemapversion)*