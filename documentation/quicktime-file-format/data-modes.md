# Data modes

**Framework**: QuickTime File Format

Data formats you use in extra information TLVs.

#### Overview

The data source field of the entry table (see [`Data table`](packet_entry/data_table.md)) indicates how the other 15 bytes of the entry are to be interpreted. Values of `0` through `4` are defined. The various data table formats are defined below.

Although there are various schemes, note that the entries in the various schemes are the same size, 16 bytes long.

#### No Op Data Mode

The data table entry has the format for no-op mode shown in the following table:

| Bit | Value |
| --- | --- |
| 0 - 7 | data source = `0` |
| 8 - 15 | ingored |

##### Field Descriptions

#### Immediate Data Mode

The data table entry has the format for immediate mode shown in the following table:

| Bit | Value |
| --- | --- |
| 0 - 7 | data source = `1` |
| 8 - 15 | immediate length |
| immediate data |  |

##### Field Descriptions

#### Sample Mode

The data table entry has the format for sample mode shown in the following table:

| Bit | Value |
| --- | --- |
| 0 - 7 | data source = `2` |
| 8 - 15 | track ref index |
| length |  |
| sample number |  |
| offset |  |
| bytes per compression block |  |
| samples per compression block |  |

##### Field Descriptions

If the bytes per compression block and/or the samples per compression block is greater than `1`, than this ratio is used to translate a sample number into an actual byte offset.

This ratio mode is typically used for compressed sound tracks. Note that for QuickTime sound tracks, the bytes per compression block also factors in the number of sound channels in that stream, so a QuickTime stereo sound stream’s BPCB would be twice that of a mono stream of the same sound format.

`(CB = NS \* BPCB / SPCB)`

where `CB` = compressed bytes, `NS` = number of samples, `BPCB` = bytes per compression block, and `SPCB` = samples per compression block.

An example:

A GSM compression block is typically 160 samples packed into 33 bytes.

So, `BPCB = 33` and `SPCB = 160`.

The hint sample requests 33 bytes of data starting at the 161st media sample. Assume that the first QuickTime chunk contains at least 320 samples. So after determining that this data will come from chunk 1, and knowing where chunk 1 starts, you must use this ratio to adjust the offset into the file where the requested samples will be found:

```c
chunk_number = 1; /* calculated by walking the sample-to-chunk atom  */
first_sample_in_this_chunk = 1; /* also calculated from that atom  */
chunk_offset = chunk_offsets[chunk_number]; /* from the stco atom  */
data_offset = (sample_number - first_sample_in_this_chunk) * BPCB  / SPCB;
read_from_file(chunk_offset + data_offset, length); /* read our  data */
```

#### Sample Description Mode

The data table entry has the format for sample description mode shown in the following table.

| Bit | Value |
| --- | --- |
| 0 - 7 | data source = `3` |
| 8 - 15 | track ref index |
| length |  |
| sample description index |  |
| offset |  |
| reserved |  |

##### Field Descriptions


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/data_modes)*