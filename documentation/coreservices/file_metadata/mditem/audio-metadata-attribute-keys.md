# Audio Metadata Attribute Keys

**Framework**: Core Services

Metadata attribute keys that describe an audio file.

## Topics

### Constants
- [let kMDItemAppleLoopDescriptors: CFString!](kmditemappleloopdescriptors.md)
  Specifies multiple pieces of descriptive information about a loop. A CFArray of CFStrings.
- [let kMDItemAppleLoopsKeyFilterType: CFString!](kmditemappleloopskeyfiltertype.md)
  Specifies key filtering information about a loop. Loops are matched against projects that often in a major or minor key. A CFString.
- [let kMDItemAppleLoopsLoopMode: CFString!](kmditemappleloopsloopmode.md)
  Specifies how a file should be played. A CFString.
- [let kMDItemAppleLoopsRootKey: CFString!](kmditemappleloopsrootkey.md)
  Specifies the loop's original key. The key is the root note or tonic for the loop, and does not include the scale type. A CFString.
- [let kMDItemAudioChannelCount: CFString!](kmditemaudiochannelcount.md)
  Number of channels in the audio data contained in the file. A CFNumber.
- [let kMDItemAudioEncodingApplication: CFString!](kmditemaudioencodingapplication.md)
  The name of the application that encoded the data contained in the audio file. A CFString.
- [let kMDItemAudioSampleRate: CFString!](kmditemaudiosamplerate.md)
  Sample rate of the audio data contained in the file. The sample rate is a float value representing hz (audio_frames/second). For example: 44100.0, 22254.54. A CFNumber.
- [let kMDItemAudioTrackNumber: CFString!](kmditemaudiotracknumber.md)
  The track number of a song or composition when it is part of an album. A CFNumber (integer).
- [let kMDItemComposer: CFString!](kmditemcomposer.md)
  The composer of the music contained in the audio file. A CFString.
- [let kMDItemIsGeneralMIDISequence: CFString!](kmditemisgeneralmidisequence.md)
  Indicates whether the MIDI sequence contained in the file is setup for use with a General MIDI device. A CFBoolean.
- [let kMDItemKeySignature: CFString!](kmditemkeysignature.md)
  The key of the music contained in the audio file. For example: C, Dm, F#m, Bb. A CFString.
- [let kMDItemLyricist: CFString!](kmditemlyricist.md)
  The lyricist, or text writer, of the music contained in the audio file. A CFString.
- [let kMDItemMusicalGenre: CFString!](kmditemmusicalgenre.md)
  The musical genre of the song or composition contained in the audio file. For example: Jazz, Pop, Rock, Classical. A CFString.
- [let kMDItemMusicalInstrumentCategory: CFString!](kmditemmusicalinstrumentcategory.md)
  Specifies the category of an instrument. A CFString.
- [let kMDItemMusicalInstrumentName: CFString!](kmditemmusicalinstrumentname.md)
  Specifies the name of instrument relative to the instrument category. A CFString.
- [let kMDItemRecordingDate: CFString!](kmditemrecordingdate.md)
  The recording date of the song or composition.
- [let kMDItemRecordingYear: CFString!](kmditemrecordingyear.md)
  Indicates the year the item was recorded. For example, 1964, 2003, etc. A CFNumber.
- [let kMDItemTempo: CFString!](kmditemtempo.md)
  A float value that specifies the beats per minute of the music contained in the audio file. A CFNumber.
- [let kMDItemTimeSignature: CFString!](kmditemtimesignature.md)
  The time signature of the musical composition contained in the audio/MIDI file. For example: "4/4", "7/8". A CFString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/audio_metadata_attribute_keys)*