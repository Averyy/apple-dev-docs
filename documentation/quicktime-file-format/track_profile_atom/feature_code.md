# Feature code

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit unsigned integer that represents a code specifying a feature.

## Overview

The third field is the feature code, or name, a 32-bit unsigned integer that is usually best interpreted as four ASCII characters. Example: the maximum video bit rate feature has a feature code or name of `'mvbr'`. It is permissible to use a feature code value of zero (`0x00000000`, not four ASCII zero characters) as a placeholder in one or more name-value pairs. The reader should ignore feature codes of value zero.

## See Also

### Data fields
- [Reserved](./reserved.md)
  A 32-bit field.
- [Part-ID](./part-id.md)
  A 32-bit field that defines the feature as being either brand-specific or universal.
- [Value](./value.md)
  A 32-bit field that represents a value related to a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_profile_atom/feature_code)*