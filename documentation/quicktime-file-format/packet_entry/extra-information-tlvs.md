# Extra information TLVs

**Framework**: QuickTime File Format  
**Kind**: property

A list of extra informtion that extends the hint track format without changing the version.

#### Overview

The extra information TLVs listed in the following table are present if and only if the X bit is set in the flags field. This provides a way of extending the hint track format without changing the version, while allowing backward compatibility.

| Extra information TLVs | Bytes |
| --- | --- |
| Extra information size | 4 |
| TLV size | 4 |
| TLV type | 4 |
| TLV data | Padded to 4-byte boundary(int(TLV Size -8 +3) / 4 * 4 |
| TLV size | 4 |
| TLV type | 4 |
| TLV data | Padded to 4-byte boundary(int(TLV Size -8 +3) / 4 * 4 |
| TLV size and so forth | … |

- **Extra information size**: A 32-bit number that is the total size of all extra information TLVs in this packet, including the 4 bytes used for this field. An empty Extra information TLVs table would just be the extra information size, having the value 4. (In this case, it would be more efficient simply to not set the X bit and save 4 bytes just to represent the empty table.)
- **TLV size**: A 32-bit number that is the total size of this one TLV entry, including 4 bytes for the size, 4 bytes for the type, and any data bytes, but not including padding required to align to the next 4 byte boundary.
- **TLV type**: A 32-bit tag (a four-character OSType) identifying the TLV. Servers must ignore TLV types that they do not recognize. Note that TLV types containing all lowercase letters are reserved by Apple.
- **TLV data**: The data for the TLV. In order to support MPEG (and other data types) whose RTP timestamp is not monotonically increasing and directly calculated from the sample timestamp, the TLV type listed in the following table is defined.

| Size | Type | Data description |
| --- | --- | --- |
| 12 | `'rtpo'` | A signed 32-bit integer to be added to the RTP timestamp, which is derived from the hint sample timestamp. |

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
- [Data table](packet_entry/data_table.md)
  A table that defines the data to be put in the payload portion of the RTP packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/packet_entry/extra_information_tlvs)*