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

#### Movie Importer Component Flags

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