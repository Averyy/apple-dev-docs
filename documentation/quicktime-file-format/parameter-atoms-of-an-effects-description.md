# Parameter atoms of an effects description

**Framework**: QuickTime File Format

Customize your effect with parameter atoms.

#### Overview

In addition to the required atoms, the effects description contains a variable number of parameter atoms. The number and types of parameter atoms vary from effect to effect. For example, the cross fade effect has only one parameter, while the general convolution filter effect has nine. Some effects have no parameters at all, and do not require any parameter atoms.

You can obtain the list of parameter atoms for a given effect by calling the effect component using `ImageCodecGetParameterList`. The parameter description atoms it returns include default settings for each parameter in the form of parameter atoms that you can insert into your effect description.

The `QTInsertChild` function is used to add these parameters to the effect description, as seen in the code example in [`Required atoms of an effects description`](required_atoms_of_an_effects_description.md).

Consider, for instance, the push effect. Its effect description contains a `kParameterWhatName` atom, two `kEffectSourceName` atoms, and two parameter atoms, one of which is a tween.

The `kParameterWhatName` atom specifies that this is a `'push'` effect.

The two `kEffectSourceName` atoms specify the two sources that this effect will use, in this case `'srcA'` and `'srcB'`. The names correspond to entries in the effect track’s input map.

The `'pcnt'` parameter atom defines which frames of the effect are shown. This parameter contains a tween entry, so that the value of this parameter is interpolated as the effect runs. The interpolation of the `'pcnt'` parameter causes consecutive frames of the effect to be rendered, creating the push effect.

The `'from'` parameter determines the direction of the push. This parameter is set from an enumeration list, with `2` being defined as the bottom of the screen.

In this example, the source `'srcB'` will push in from the bottom, covering the source `'srcA'`.

The `'pcnt'` parameter is normally tweened from `0` to `100`, so that the effect renders completely, from `0` to `100` percent. In this example, the `'pcnt'` parameter is tweened from `25` to `75`, so the effect will start `25` percent of the way through (with `'srcB'` already partly on screen) and finish `75` percent of the way through (with part of `'srcA'` still visible).

An important property of effect parameters is that most can be tweened (and some must be tweened). Tweening is QuickTime’s general purpose interpolation mechanism (see [`Tween media`](tween_media.md) for more information). For many parameters, it is desirable to allow the value of the parameter to change as the effect executes. In the example shown in preceeding figure, the `'pcnt'` parameter must be a tween. This parameter controls which frame of the effect is rendered at any given time, so it must change for the effect to progress. The `'from'` parameter is not a tween in the example above, but it could be if we wanted the direction of the push to change during the course of the effect.

## See Also

- [Structure of an effect description](structure_of_an_effect_description.md)
  An effect description is the sole media sample for an effect track.
- [Required atoms of an effects description](required_atoms_of_an_effects_description.md)
  Specify the required atoms for your effects description.
- [Creating an input map](creating_an_input_map.md)
  Describe and name sources with an input map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/parameter_atoms_of_an_effects_description)*