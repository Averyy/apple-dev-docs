# Sample-to-group atom ('sbpd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that associates a sample with a sample group description.

## Mentions

- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)

#### Overview

Sample-to-group atoms are used to find the group that a sample belongs to and the associated description of that sample group. The sample-to-group atom has an atom type of `‘sbgp’`.

In a general case, there may be multiple instances of sample-to-group atoms if there is more than one sample grouping for the samples in a track. Each instance of the sample-to group atom has a grouping type code that distinguishes different sample groupings. Within a track there can be at most one instance of this atom with a particular grouping type. An associated sample group description atom indicates the same value for the grouping type.

The sample-to-group atom contains a table with a sample count and group description index pairs. The sample count is the number of media samples in the run of samples with the same sample group description. The group description index is an index into the array of payload data entries in the associated sample group description atom’s payload data table, the association defined by having the same grouping type value.

For use in AAC encoder delay representation, there is one sample-to-group atom instance in a given QuickTime sound track with grouping type `‘roll’` matching the single instance of the sample group description atom. The entry count field value is set to `1`, indicating one entry in the table data array. That entry is describing all the AAC packets in the track. The sample count in the table data array is typically the same as the sample size atom’s number of entries field, see [`Sample size atom ('stsz')`](sample_size_atom.md), which represents the number of media samples in the track (in this use, AAC packets). For AAC encoder delay representation, the only entry in the associated sample group description atom’s payload data table is the first, which provides the value of 1 for the group description index.

The layout of the sample-to-group atom is as follows:

| Sample-to-group atom | Bytes |
| --- | --- |
| [`Size`](sample-to-group_atom/size.md) | 4 |
| [`Type`](sample-to-group_atom/type.md) = `'sbgp'` | 4 |
| [`Version`](sample-to-group_atom/version.md) | 1 |
| [`Flags`](sample-to-group_atom/flags.md) | 3 |
| [`Grouping type`](sample-to-group_atom/grouping_type.md) | 4 |
| [`Default length`](sample-to-group_atom/default_length.md) | 4 |
| [`Entry count`](sample-to-group_atom/entry_count.md) | 4 |
| [`Table data`](sample-to-group_atom/table_data.md) | variable |

## Topics

### Data fields
- [Size](sample-to-group_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sample-to-group atom.
- [Type](sample-to-group_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sample-to-group_atom/version.md)
  A 1-byte specification of the version of this sample-to-group atom.
- [Flags](sample-to-group_atom/flags.md)
  A 3-byte reserved space.
- [Grouping type](sample-to-group_atom/grouping_type.md)
  A 32-bit integer identifying the grouping type.
- [Default length](sample-to-group_atom/default_length.md)
  A 32-bit integer indicating the length of the group entry in the payload data.
- [Entry count](sample-to-group_atom/entry_count.md)
  A 32-bit integer giving the number of entries in the table data that follows.
- [Table data](sample-to-group_atom/table_data.md)
  A table of sample count and group description index pairs.

## See Also

- [Sample group description atom ('sgpd')](sample_group_description_atom.md)
  An atom that gives information about the characteristics of sample groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample-to-group_atom)*