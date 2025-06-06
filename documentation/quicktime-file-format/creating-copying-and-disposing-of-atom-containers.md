# Creating, copying, and disposing of atom containers

**Framework**: QuickTime File Format

Manage atoms in atom containers.

#### Overview

Before you can add atoms to an atom container, you must first create the container by calling `QTNewAtomContainer`. The code sample shown in the following calls `QTNewAtomContainer` to create an atom container.

```c
QTAtomContainer spriteData;
OSErr err
// Create an atom container to hold a sprite’s data.
err=QTNewAtomContainer (&spriteData);
```

When you have finished using an atom container, dispose of it by calling the `QTDisposeAtomContainer` function. The sample code shown in the following listing calls `QTDisposeAtomContainer` to dispose of the `spriteData` atom container.

```c
if (spriteData)
    QTDisposeAtomContainer (spriteData);
```

## Topics

### Managing atoms
- [Creating new atoms](creating_new_atoms.md)
  Create new atoms and insert them in a QT atom container.
- [Copying existing atoms](copying_existing_atoms.md)
  Copy existing atoms within an atom container.
- [Retrieving atoms from an atom container](retrieving_atoms_from_an_atom_container.md)
  Retrieve information about the types of a parent atom’s children, search for a specific atom, and retrieve a leaf atom’s data.
- [Modifying atoms](modifying_atoms.md)
  Modify attributes or data associated with an atom in an atom container.
- [Removing atoms from an atom container](removing_atoms_from_an_atom_container.md)
  Remove atoms from an atom container.

## See Also

- [Atoms](atoms.md)
  The basic data unit in a QuickTime file is the atom.
- [QT atoms and atom containers](qt_atoms_and_atom_containers.md)
  An enhanced data structure that provide a more general-purpose storage format.
- [QuickTime movie files](quicktime_movie_files.md)
  The QuickTime file format describes the characteristics of QuickTime movie files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/creating_copying_and_disposing_of_atom_containers)*