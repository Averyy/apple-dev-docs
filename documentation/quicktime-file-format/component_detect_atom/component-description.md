# Component description

**Framework**: QuickTime File Format  
**Kind**: property

A component description record.

#### Overview

Describes a class of components by their attributes. Fields that are set to `0` are treated as “don’t care.”

```objc
struct ComponentDescription {
	OSType componentType;
	OSType componentSubType;
	OSType componentManufacturer;
	unsigned long componentFlags;
	unsigned long componentFlagsMask;
};
```

- **`componentType`**: A four-character code that identifies the type of component.
- **`componentSubType`**: A four-character code that identifies the subtype of the component. For example, the subtype of an image compressor component indicates the compression algorithm employed by the compressor. A value of `0` matches any subtype.
- **`componentManufacturer`**: A four-character code that identifies the manufacturer of the component. Components provided by Apple have a manufacturer value of `'appl'`. A value of `0` matches any manufacturer.
- **`componentFlags`**: A 32-bit field that contains flags describing required component capabilities. Set the high-order 8 bits to `0`. The low-order 24 bits are specific to each component type. These flags can be used to indicate the presence of features or capabilities in a given component.
- **`componentFlagsMask`**: A 32-bit field that indicates which flags in the `componentFlags` field are relevant to this operation. For each flag in the `componentFlags` field that is to be considered as a search criterion, set the corresponding bit in this field to `1`. To ignore a flag, set the bit to `0`.

#### Movie Importer Component Flags

- **`canMovieImportInPlace`**: Set this bit if a movie import component must be able to create a movie from a file without having to write to a separate disk file. Examples include MPEG and AIFF import components.
- **`movieImportSubTypeIsFileExtension`**: Set this bit if the component’s subtype is a file extension instead of a Macintosh file type. For example, if you require an import component that opens files with an extension of `.doc`, set this flag and set your component subtype to `'DOC '`.
- **`canMovieImportFiles`**: Set this bit if a movie import component must import files.

## See Also

- [Size](component_detect_atom/size.md)
  The number of bytes in this component detect atom.
- [Type](component_detect_atom/type.md)
  The type of this atom.
- [Flags](component_detect_atom/flags.md)
  A 32-bit integer.
- [Minimum version](component_detect_atom/minimum_version.md)
  An unsigned 32-bit integer containing the minimum required version of the specified component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/component_detect_atom/component_description)*