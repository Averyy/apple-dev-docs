# Creating an input map

**Framework**: QuickTime File Format

Describe and name sources with an input map.

#### Overview

The input map is another QT atom container that you attach to the effects track. It describes the sources used in the effect and gives a name to each source. This name is used to refer to the source in the effects description.

An input map works in concert with track reference atoms in the source tracks. A track reference atom of type `kTrackModifierReference` is added to each source track, which causes that source track’s output to be redirected to the effects track. An input map is added to the effects track to identify the source tracks and give a name to each source, such as `'srcA'` and `'srcB'`. The effect can then refer to the sources by name, specifying that `'srcB'` should slide in over `'srcA'`, for example.

#### Structure of an Input Map

The input map contains a set of atoms that refer to the tracks used as sources for the effect. Each source track is represented by one track reference atom of type `kTrackModifierInput`.

Each modifier input atom contains two children, one of type `kEffectDataSourceType`, and one of type `kTrackModifierType`, which hold the name and type of the source.

The name of the source is a unique identifier that you create, which is used in the effect description to reference the track. Any four-character name is valid, as long as it is unique in the set of source names.

> ❗ **Important**: Apple recommends you adopt the standard naming convention `'srcX'`, where X is a letter of the alphabet. Thus, your first source would be named `'srcA'`, the second ’`srcB'`, and so forth.

Apple recommends you adopt the standard naming convention `'srcX'`, where X is a letter of the alphabet. Thus, your first source would be named `'srcA'`, the second ’`srcB'`, and so forth.

The child atom of type `kTrackModifierType` indicates the type of the track being referenced. For a video track the type is `VideoMediaType`, for a sprite track it is `SpriteMediaType`, and so forth. Video tracks are the most common track type used as sources for effects. Only tracks that have a visible output, such as video and sprite tracks, can be used as sources for an effect. This means, for example, that sound tracks cannot be sources for an effect.

You refer to a `kTrackModifierInput` atom by its index number, which is returned by the `AddTrackReference` function when you create the atom.

#### Building Input Maps

The first step in creating an input map is to create a new `QTAtomContainer` to hold the map. You use the standard QuickTime container creation function.

```c
QTNewAtomContainer(&inputMap);
```

For each source you are creating, call the `AddTrackReference` function. The track IDs of the effects track and the source track are passed as parameters to `AddTrackReference`, which creates an atom of type `kTrackModifierReference` and returns an index number. You use this index as the ID of the atom when you need to refer to it. You then insert the reference into the input map as an atom of type `kTrackModifierInput`.

The code in following listing creates a reference to the track `firstSourceTrack`, and adds it to the input map.

```c
AddTrackReference(theEffectsTrack, firstSourceTrack,
                 kTrackModifierReference, &referenceIndex);
 
QTInsertChild(inputMap, kParentAtomIsContainer,
            kTrackModifierInput, referenceIndex, 0, 0, nil, &inputAtom);
```

The `QTInsertChild` function returns the offset of the new modifier input atom in the `inputAtom` parameter.

Add the name and type of the source track to the modifier input atom. Again, calling the `QTInsertChild` function does this, as shown in the following code snippet:

```c
inputType = VideoMediaType;
QTInsertChild(inputMap, inputAtom,
                kTrackModifierType, 1, 0, sizeof(inputType), &inputType,
                nil);
 
aType = 'srcA';
QTInsertChild(inputMap, inputAtom, kEffectDataSourceType, 1, 0,
            sizeof(aType), &aType, nil);
```

This process is repeated for each source for the effect.

## See Also

- [Structure of an effect description](structure_of_an_effect_description.md)
  An effect description is the sole media sample for an effect track.
- [Required atoms of an effects description](required_atoms_of_an_effects_description.md)
  Specify the required atoms for your effects description.
- [Parameter atoms of an effects description](parameter_atoms_of_an_effects_description.md)
  Customize your effect with parameter atoms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/creating_an_input_map)*