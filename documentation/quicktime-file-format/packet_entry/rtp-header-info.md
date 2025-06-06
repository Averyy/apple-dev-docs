# RTP header info

**Framework**: QuickTime File Format  
**Kind**: property

A 16-bit integer specifying various values to be set in the RTP header.

#### Overview

The bits of the field are defined as follows.

| Bit | Value |
| --- | --- |
| 0 | reserved |
| 1 | reserved |
| 2 | P |
| 3 | X |
| 4 | reserved |
| 5 | reserved |
| 6 | reserved |
| 7 | reserved |
| 8 | M |
| 9 | payload type |
| 0 | payload type |
| 1 | payload type |
| 2 | payload type |
| 3 | payload type |
| 4 | payload type |
| 5 | payload type |

The RTP header information field contains the elements as follows:

| Field | Bit# | Description |
| --- | --- | --- |
| P | 2 | A 1-bit number corresponding to the padding (P) bit in the RTP header. This bit should probably not be set, since a server that needs different packet padding would need to unpad and repad the packet itself. |
| X | 3 | A 1-bit number corresponding to the extension (X) bit in the RTP header. This bit should probably not be set, since a server that needs to send its own RTP extension would either not be able to, or would be forced to replace any extensions from the hint track. |
| M | 8 | A 1-bit number corresponding to the marker (M) bit in the RTP header. |
| Payload type | 9-15 | A 7-bit number corresponding to the payload type (PT) field of the RTP header. |

All undefined bits are reserved and must be set to zero. Note that the location of the defined bits are in the same bit location as in the RTP header.

## See Also

- [Relative packet transmission time](packet_entry/relative_packet_transmission_time.md)
  A 32-bit signed integer value, indicating the time, in the hint track’s time scale, to send this packet relative to the hint sample’s actual time.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/packet_entry/rtp_header_info)*