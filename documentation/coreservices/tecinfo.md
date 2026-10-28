# TECInfo

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Contains information about the Unicode Converter, the Text Encoding Converter, and Basic Text Types.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct TECInfo {
    ...
} TECInfo;
```

## Overview

The converter information structure is used by the function [`TECGetInfo`](./api-1400430-tecgetinfo.md) to hold returned information about the Unicode Converter, the Text Encoding Converter, and Basic Text Types.  

## Topics

### Instance Properties
- [format](./tecinfo/api-1399752-format.md)
  The current format of the returned structure. The format of the structure is indicated by the `kTECInfoCurrentFormat` constant. Any future changes to the format will always be backwardly compatible; any new fields will be added to the end of the structure.
- [tecExtensionFileName](./tecinfo/api-1400210-tecextensionfilename.md)
  A Pascal string with the (possibly localized) name of the Text Encoding Conversion Manager extension file.
- [tecHighestTEFileVersion](./tecinfo/api-1399847-techighesttefileversion.md)
- [tecLowestTEFileVersion](./tecinfo/api-1399715-teclowesttefileversion.md)
- [tecTextCommonFeatures](./tecinfo/api-1400184-tectextcommonfeatures.md)
  Bit flags indicating new features or bug fixes in Basic Text Types (the Text Common static library). No bits are currently defined.
- [tecTextConverterFeatures](./tecinfo/api-1400170-tectextconverterfeatures.md)
  New features or bug fixes in the Text Encoding Converter. No bits are currently defined.
- [tecTextEncodingsFolderName](./tecinfo/api-1399788-tectextencodingsfoldername.md)
  A Pascal string with the (possibly localized) name of the Text Encodings folder.
- [tecUnicodeConverterFeatures](./tecinfo/api-1399691-tecunicodeconverterfeatures.md)
  Bit flags indicating new features or bug fixes in the Unicode Converter. See [Unicode Converter Flags](./api-1400304-unicode_converter_flags.md) for the currently defined bit flags.
- [tecVersion](./tecinfo/api-1400200-tecversion.md)
  The current version of the Text Encoding Conversion Manager extension in BCD (binary coded decimal), with the first byte indicating the major version; for example, 0x0121 for 1.2.1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecinfo)*