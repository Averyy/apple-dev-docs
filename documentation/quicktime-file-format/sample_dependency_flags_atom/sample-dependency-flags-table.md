# Sample dependency flags table

**Framework**: QuickTime File Format  
**Kind**: property

A table of 8-bit values indicating the sample flag settings.

#### Overview

The number of entries in the table is obtained from the associated sample size atom’s number of samples field.

An example of a sample dependency flags table is as follows.

| Sample dependency flag | Sample |
| --- | --- |
| Flags | Sample 1 |
| Flags | Sample 2 |
| Flags | Sample 3 |
| Flags | Sample 4 |
| Flags | Sample 5 |

Flag values are specified as follows.

```objc
enum {
// bit 0x80 is reserved; bit combinations 0x30, 0xC0 and 0x03 are reserved
kQTSampleDependency_EarlierDisplayTimesAllowed = 1<<6, // mediaSampleEarlierDisplayTimesAllowed
kQTSampleDependency_SampleDoesNotDependOnOthers = 1<<5, // ie: an I picture
kQTSampleDependency_SampleDependsOnOthers = 1<<4, // ie: not an I picture
kQTSampleDependency_NoOtherSampleDependsOnThisSample = 1<<3,  // mediaSampleDroppable
kQTSampleDependency_OtherSamplesDependOnThisSample = 1<<2,
kQTSampleDependency_ThereIsNoRedundantCodingInThisSample = 1<<1,
kQTSampleDependency_ThereIsRedundantCodingInThisSample = 1<<0
};
```

## See Also

- [Size](sample_dependency_flags_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the sample dependency flags atom.
- [Type](sample_dependency_flags_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sample_dependency_flags_atom/version.md)
  A 1-byte specification of the version of this atom.
- [Flags](sample_dependency_flags_atom/flags.md)
  A 3-byte space reserved for flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_dependency_flags_atom/sample_dependency_flags_table)*