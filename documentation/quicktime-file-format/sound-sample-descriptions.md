# Sound sample descriptions

**Framework**: QuickTime File Format

A sound sample description contains information that defines how to interpret sound media data.

#### Overview

The sound sample description contains information that defines how to interpret sound media data. This sample description is based on the standard sample description, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

The data format field contains the format of the audio data. This may specify a compression format or one of several uncompressed audio formats. The following table shows a list of some supported sound formats.

| Format | 4-character code | Description |
| --- | --- | --- |
| Not specified | `0x00000000` | This format descriptor should not be used, but may be found in some files. Samples are assumed to be stored in either `'raw '` or `'twos'` format, depending on the sample size field in the sound description. |
| `kSoundNotCompressed` | `'NONE'` | This format descriptor should not be used, but may be found in some files. Samples are assumed to be stored in either `'raw '` or `'twos'` format, depending on the sample size field in the sound description. |
| `k8BitOffsetBinaryFormat` | `'raw '` | Samples are stored uncompressed, in offset-binary format (values range from `0` to `255`; `128` is silence). These are stored as 8-bit offset binaries. |
| `k16BitBigEndianFormat` | `'twos'` | Samples are stored uncompressed, in two’s-complement format (sample values range from `-128` to `127` for 8-bit audio, and `-32768` to `32767` for 1-bit audio; `0` is always silence). These samples are stored in 16-bit big-endian format. |
| `k16BitLittleEndianFormat` | `'sowt'` | 16-bit little-endian, twos-complement |
| `kMACE3Compression` | `'MAC3 '` | Samples have been compressed using MACE 3:1. (Obsolete.) |
| `kMACE6Compression` | `'MAC6 '` | Samples have been compressed using MACE 6:1. (Obsolete.) |
| `kIMACompression` | `'ima4'` | Samples have been compressed using IMA 4:1. |
| `kFloat32Format` | `'fl32'` | 32-bit floating point |
| `kFloat64Format` | `'fl64'` | 64-bit floating point |
| `k24BitFormat` | `'in24'` | 24-bit integer |
| `k32BitFormat` | `'in32'` | 32-bit integer |
| `kULawCompression` | `'ulaw'` | uLaw 2:1 |
| `kALawCompression` | `'alaw'` | uLaw 2:1 |
| `kMicrosoftADPCMFormat` | `0x6D730002` | Microsoft ADPCM-ACM code 2 |
| `kDVIIntelIMAFormat` | `0x6D730011` | DVI/Intel IMAADPCM-ACM code 17 |
| `kDVAudioFormat` | `'dvca'` | DV Audio |
| `kQDesignCompression` | `'QDMC'` | QDesign music |
| `kQDesign2Compression` | `'QDM2'` | QDesign music version 2 |
| `kQUALCOMMCompression` | `'Qclp'` | QUALCOMM PureVoice |
| `kMPEGLayer3Format` | `0x6D730055` | MPEG-1 layer 3, CBR only (pre-QT4.1) |
| `kFullMPEGLay3Format` | `'.mp3'` | MPEG-1 layer 3, CBR & VBR (QT4.1 and later) |
| `kMPEG4AudioFormat` | `'mp4a'` | MPEG-4, Advanced Audio Coding (AAC) |
| `kAC3AudioFormat` | `'ac-3'` | Digital Audio Compression Standard (AC-3, Enhanced AC-3) |

## Topics

### Using sample descriptions
- [Sound sample description version 0 ('stsd')](sound_sample_description_version_0.md)
  A sound sample description that supports only uncompressed audio in raw or twos-complement format.
- [Sound sample description version 1 ('stsd')](sound_sample_description_version_1.md)
  An extended sound sample description that supports compressed audio, and includes the ability to add atoms to the sound description.
- [Sound sample description version 2 ('stsd')](sound_sample_description_version_2.md)
  An updated sound sample description that adds high resolution audio.

## See Also

- [Sound sample description extensions](sound_sample_description_extensions.md)
  Extend sound sample descriptions by appending other atoms.
- [Sound sample data](sound_sample_data.md)
  Sound sample formats that QuickTime supports.
- [Audio priming-handling encoder delay in AAC](appendix_g_audio_priming_handling_encoder_delay_in_aac.md)
  Position a source audio signal in a sound track to handle encoder delay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_sample_descriptions)*