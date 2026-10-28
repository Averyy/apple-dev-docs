# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit unsigned integer value.

## Overview

Set to `'ctry'`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Version](./version.md)
  One byte.
- [Flags](./flags.md)
  Three bytes.
- [Entry_count](./entry_count.md)
  A 32-bit integer indicating the number of Country arrays to follow in this atom.
- [Country_count](./country_count.md)
  A 16-bit integer indicating the number of Countries in the array.
- [Country[Country_count]](./country_country_count.md)
  An array of 16-bit integers, defined according to the ISO 3166 definition of country codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/country_list_atom/type)*