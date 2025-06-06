# Structure of an effect description

**Framework**: QuickTime File Format

An effect description is the sole media sample for an effect track.

#### Overview

An effect description is implemented as a `QTAtomContainer` structure, the general QuickTime structure for holding a set of QuickTime atoms. All effect descriptions must contain the set of required atoms, which specify attributes such as which effect component to use. In addition, effect descriptions can contain a variable number of parameter atoms, which hold the values of the parameters for the effect.

Each atom contains either data or a set of child atoms. If a parameter atom contains data, the data is the value of the parameter, and this value remains constant while the effect executes. If a parameter atom contains a set of child atoms, they typically contain a tween entry so the value of the parameter will be interpolated for the duration of the effect.

You assemble an effect description by adding the appropriate set of atoms to a `QTAtomContainer` structure.

You can find out what the appropriate atoms are by making an `ImageCodecGetParameterList` call to the effect component. This fills an atom container with a set of parameter description atoms. These atoms contain descriptions of the effect parameters, such as each parameter’s atom type, data range, default value, and so on. The default value in each description atom is itself a `QTAtom` that can be inserted directly into your effect description.

You can modify the data in the parameter atoms directly, or let the user set them by calling `QTCreateStandardParameterDialog`, which returns a complete effect description (you need to add `kEffectSourceName` atoms for effects that require sources).

You then add the effect description to the media of the effect track.

## See Also

- [Required atoms of an effects description](required_atoms_of_an_effects_description.md)
  Specify the required atoms for your effects description.
- [Parameter atoms of an effects description](parameter_atoms_of_an_effects_description.md)
  Customize your effect with parameter atoms.
- [Creating an input map](creating_an_input_map.md)
  Describe and name sources with an input map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/structure_of_an_effect_description)*