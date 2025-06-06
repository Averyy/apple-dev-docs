# Feature code

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit unsigned integer that represents a code specifying a feature.

#### Overview

The third field is the feature code, or name, a 32-bit unsigned integer that is usually best interpreted as four ASCII characters. Example: the maximum video bit rate feature has a feature code or name of `'mvbr'`. It is permissible to use a feature code value of zero (`0x00000000`, not four ASCII zero characters) as a placeholder in one or more name-value pairs. The reader should ignore feature codes of value zero.

## See Also

- [Reserved](track_profile_atom/reserved.md)
  A 32-bit field.
- [Part-ID](track_profile_atom/part-id.md)
  A 32-bit field that defines the feature as being either brand-specific or universal.
- [Value](track_profile_atom/value.md)
  A 32-bit field that represents a value related to a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_profile_atom/feature_code)*