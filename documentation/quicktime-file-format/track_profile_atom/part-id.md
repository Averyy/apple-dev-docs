# Part-ID

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit field that defines the feature as being either brand-specific or universal.

#### Overview

The second field is the part-ID, which defines the feature as being either brand-specific or universal. Brand-specific features are particular to a specific brand. Universal features can be found in any file type that uses the profile atom. Universal features have a part-ID of four ASCII spaces (`0x20202020`). Brand-specific features have a part-ID that is one of the compatible brand codes for that file type, as specified in the file type atom (`'ftyp'`). For example, the part-ID for QuickTime-specific features is `'qt '`. All features described in this documentation, however, are universal.

## See Also

- [Reserved](track_profile_atom/reserved.md)
  A 32-bit field.
- [Feature code](track_profile_atom/feature_code.md)
  A 32-bit unsigned integer that represents a code specifying a feature.
- [Value](track_profile_atom/value.md)
  A 32-bit field that represents a value related to a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_profile_atom/part-id)*