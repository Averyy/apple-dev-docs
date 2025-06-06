# Entry count

**Framework**: QuickTime File Format  
**Kind**: property

A 16-bit unsigned integer indicating the number of packet entries in the table.

#### Overview

Each entry in the table corresponds to a packet. Multiple entries in a single sample indicate that the media sample had to be split into multiple packets. A sample with an entry count of `0` is reserved and, if encountered, must be skipped.

## See Also

- [Reserved](packetization_hint_sample_data/reserved.md)
  Two bytes.
- [Packet entry table](packetization_hint_sample_data/packet_entry_table.md)
  A variable length table containing packet entries.
- [Additional data](packetization_hint_sample_data/additional_data.md)
  A variable length field containing data pointed to by the entries in the data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/packetization_hint_sample_data/entry_count)*