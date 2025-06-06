# Data table

**Framework**: QuickTime File Format  
**Kind**: property

A table that defines the data to be put in the payload portion of the RTP packet.

## Mentions

- [Data modes](data_modes.md)

#### Overall

This table defines various places the data can be retrieved. Table entries are listed in the following table.

| Data table entry | Bytes |
| --- | --- |
| Data source | 1 |
| Data | 15 |

The data source field of the entry table indicates how the other 15 bytes of the entry are to be interpreted. Values of `0` through `4` are defined. The various data table formats are defined in [`Data modes`](data_modes.md).

Although there are various schemes, note that the entries in the various schemes are the same size, 16 bytes long.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/packet_entry/data_table)*