# Relative packet transmission time

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit signed integer value, indicating the time, in the hint track’s time scale, to send this packet relative to the hint sample’s actual time.

#### Overview

Negative values mean that the packet will be sent earlier than real time, which is useful for smoothing the data rate. Positive values are useful for repeating packets at later times. Within each hint sample track, each packet time stamp must be non-decreasing.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/packet_entry/relative_packet_transmission_time)*