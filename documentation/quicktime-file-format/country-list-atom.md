# Country list atom ('ctry')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that lists items that are suitable for more than one country.

#### Overview

When one or more items must be identified as being suitable for more than one country, each list of countries is stored in this otherwise optional atom. The country list atom is a full atom with an atom type of `‘ctry’`.

Each list starts with a two-byte count of the number of items in the list, and then each ISO 3166 code representing countries in the list.

The atom consists of a count of the number of lists, expressed as a 32-bit integer, and then these lists, appended end-to-end.

Note that:

- Indexes into the country list atom are 1-based.
- Zero (0) is reserved and never used as an index.
- Currently, there is a limit of 255 countries that may be recorded in a country list atom.

An example country list atom consisting of two country lists with two and three countries, respectively, is shown in the following table.

| Field size | Field | Field contents | Comment |
| --- | --- | --- | --- |
| 32-bit | atom_size | 26 | Size of this country list atom in bytes. |
| 32-bit | atom_type | `'ctry'` |  |
| 32-bit | entry_count | 2 | Number of country lists. |
| 16-bit | country_count | 2 | Number of countries in country list 1. |
| 16-bit | country | ‘US’ |  |
| 16-bit | country | ‘UK’ |  |
| 16-bit | country_count | 3 | Number of countries in country list 2. |
| 16-bit | country | ‘JP’ |  |
| 16-bit | country | ‘US’ |  |
| 16-bit | country | ‘FR’ |  |

## Topics

### Data fields
- [Size](country_list_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](country_list_atom/type.md)
  A 32-bit unsigned integer value.
- [Version](country_list_atom/version.md)
  One byte.
- [Flags](country_list_atom/flags.md)
  Three bytes.
- [Entry_count](country_list_atom/entry_count.md)
  A 32-bit integer indicating the number of Country arrays to follow in this atom.
- [Country_count](country_list_atom/country_count.md)
  A 16-bit integer indicating the number of Countries in the array.
- [Country[Country_count]](country_list_atom/country_country_count.md)
  An array of 16-bit integers, defined according to the ISO 3166 definition of country codes.

## See Also

- [Language list atom ('lang')](language_list_atom.md)
  An atom that lists items that are suitable for more than one language.
- [Metadata item keys atom ('keys')](metadata_item_keys_atom.md)
  An atom that holds a list of the metadata keys that may be present in the metadata atom.
- [Metadata item list atom ('ilst')](metadata_item_list_atom.md)
  An atom that holds a list of actual metadata values that are present in the metadata atom.
- [Metadata item atom](metadata_item_atom.md)
  An atom that holds a metadata value.
- [Value atom](value_atom.md)
  An atom that expresses a metadata value.
- [Item information atom ('itif')](item_information_atom.md)
  An atom that contains information about the item, including item-specific flags and item optional identifier.
- [Name atom ('name')](name_atom.md)
  An atom you use to provide a name for a metadata item.
- [Data atom ('data')](data_atom.md)
  An atom that contains the type and locale specific value of metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/country_list_atom)*