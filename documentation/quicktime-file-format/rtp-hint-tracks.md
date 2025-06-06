# RTP hint tracks

**Framework**: QuickTime File Format

Allow a streaming server to create RTP streams from a QuickTime movie.

#### Overview

RTP hint tracks contain information that allows a streaming server to create RTP streams from a QuickTime movie, without requiring the server to know anything about the media type, compression, or payload format.

In RTP, each media stream, such as an audio or video track, is sent as a separate RTP stream. Consequently, each media track in the movie has an associated RTP hint track containing the data necessary to packetize it for RTP transport, and each hint track contains a track reference back to its associated media track.

Media tracks that do not have an associated RTP hint track cannot be streamed over RTP. RTP streaming servers ignore them.

It is possible for a media track to have more than one associated hint track. The hint track contains information such as the packet size and time scale in the hint track’s sample description. This minimizes the runtime server load, but in order to support multiple packet sizes it is necessary to have multiple RTP hint tracks for each media track, each with different a packet size. A similar mechanism could be used to provide hint tracks for multiple protocols in the future.

It is also possible for a single hint track to refer to more than one media stream. For example, audio and video MPEG elementary streams could be multiplexed into a single systems stream RTP payload format, and a single hint track would contain the necessary information to combine both elementary streams into a single series of RTP packets.

This is the exception rather than the rule, however. In general, multiplexing is achieved by using IP’s port-level multiplexing, not by interleaving the data from multiple streams into a single RTP session.

The hint track is related to each base media track by a track reference declaration. The sample description for RTP declares the maximum packet size that this hint track will generate. Partial session description (SDP) information is stored in the track’s user data atom.

## See Also

- [Hint media](hint_media.md)
  Provide information about data units to stream in hint tracks.
- [Finding an original media track from a hint track](finding_an_original_media_track_from_a_hint_track.md)
  Use track reference atoms from hint tracks to locate the original media track.
- [Hint track sample description](hint_track_sample_description.md)
  An atom that specifies the data format and location of the hint track sample data.
- [Packetization hint sample data](packetization_hint_sample_data.md)
  An atom that describes the sample data for data using the Real-Time Transport Protocol (RTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/rtp_hint_tracks)*