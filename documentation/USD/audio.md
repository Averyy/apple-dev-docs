# audio

**Framework**: USD

The location of an audio file.

#### Overview

The default value is blank. Each instance of `AudioAction` must supply its own value for this property and an accompanying music file by the same name within the asset.

##### Declaration

```other
uniform asset audio
```

##### Define an Audio File

The following line shows how to define a path to an audio file named `backgroundMusic.m4a`:

```other
uniform asset audio = @backgroundMusic.m4a@
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [gain](gain.md)
  A value that controls the audio volume.
- [auralMode](auralmode.md)
  An option that controls the audio signal’s spacial dynamics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/audio)*