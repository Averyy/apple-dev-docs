# Packet entry

**Framework**: QuickTime File Format  
**Kind**: class

A packet entry.

#### Overview

The packet entry contains the data elements listed in the following table.

| Packet entry | Bytes |
| --- | --- |
| [`Relative packet transmission time`](packet_entry/relative_packet_transmission_time.md) | 4 |
| [`RTP header info`](packet_entry/rtp_header_info.md) | 2 |
| [`RTP sequence number`](packet_entry/rtp_sequence_number.md) | 2 |
| [`Flags`](packet_entry/flags.md) | 2 |
| [`Entry count`](packet_entry/entry_count.md) | 2 |
| [`Extra information TLVs`](packet_entry/extra_information_tlvs.md) | 0 or variable |
| [`Data table`](packet_entry/data_table.md) | variable |

## Topics

### Data fields
- [Relative packet transmission time](packet_entry/relative_packet_transmission_time.md)
  A 32-bit signed integer value, indicating the time, in the hint track’s time scale, to send this packet relative to the hint sample’s actual time.
- [RTP header info](packet_entry/rtp_header_info.md)
  A 16-bit integer specifying various values to be set in the RTP header.
- [RTP sequence number](packet_entry/rtp_sequence_number.md)
  A 16-bit integer specifying the RTP sequence number for this packet.
- [Flags](packet_entry/flags.md)
  A 16-bit field indicating certain attributes for this packet.
- [Entry count](packet_entry/entry_count.md)
  A 16-bit unsigned integer specifying the number of entries in the data table.
- [Extra information TLVs](packet_entry/extra_information_tlvs.md)
  A list of extra informtion that extends the hint track format without changing the version.
- [Data table](packet_entry/data_table.md)
  A table that defines the data to be put in the payload portion of the RTP packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/packet_entry)*