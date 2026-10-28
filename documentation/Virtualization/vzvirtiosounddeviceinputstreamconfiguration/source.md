# source

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

An audio stream source that defines how the host supplies audio data for the guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var source: VZAudioInputStreamSource? { get set }
```

```objc
@property (strong, nullable) VZAudioInputStreamSource * source;
```

## Discussion

Not specifying a source results in a default handler that produces audio silence. The default is `nil`.

## See Also

### Related Documentation
- [class VZAudioInputStreamSource](../vzaudioinputstreamsource.md)
  The base class for an audio input stream source.
- [class VZHostAudioInputStreamSource](../vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddeviceinputstreamconfiguration/source)*