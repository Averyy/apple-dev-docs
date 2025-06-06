# Adding custom atoms in a QuickTime VR movie

**Framework**: QuickTime File Format

Provide additional information about a QuickTime VR movie using custom atoms.

#### Overview

If you author a QuickTime VR movie, you may choose to add custom atoms to either the VR world or node information atom containers. Those atoms can be extracted within an application to provide additional information that the application may use.

Information that pertains to the entire scene might be stored in a custom atom within the VR world atom container. Node-specific information could be stored in the individual node information atom containers or as sibling atoms to the node location atoms within the VR world.

Custom hot spot atoms should be stored as siblings to the hot spot information atoms in the node information atom container. Generally, its atom type is the same as the custom hot spot type. You can set up an intercept procedure in your application in order to process clicks on the custom hot spots.

If you use custom atoms, you should install your hot spot intercept procedure when you open the movie. The following listing is an example of such an intercept procedure.

```c
QTVRInterceptProc MyProc = NewQTVRInterceptProc (MyHotSpot);
QTVRInstallInterceptProc (qtvr, kQTVRTriggerHotSpotSelector, myProc,  0, 0);
 
pascal void MyHotSpot (QTVRInstance qtvr, QTVRInterceptPtr qtvrMsg,
                        SInt32 refCon, Boolean *cancel)
{
    UInt32 hotSpotID = (UInt32) qtvrMsg->parameter[0];
    QTAtomContainer nodeInfo =
            (QTAtomContainer) qtvrMsg->parameter[1];
    QTAtom hotSpotAtom = (QTAtom) qtvrMsg->parameter[2];
    OSType hotSpotType;
    CustomData myCustomData;
    QTAtom myAtom;
 
    QTVRGetHotSpotType (qtvr, hotSpotID, &hotSpotType);
    if (hotSpotType != kMyAtomType) return;
 
    // It's our type of hot spot - don't let anyone else handle  it
    *cancel = true;
 
    // Find our custom atom
    myAtom = QTFindChildByID (nodeInfo, hotSpotAtom, kMyAtomType,  1, nil);
    if (myAtom != 0) {
        OSErr err;
        // Copy the custom data into our structure
        err = QTCopyAtomDataToPtr (nodeInfo, myAtom, false,
                        sizeof(CustomData), &myCustomData, nil);
        if (err == noErr)
            // Do something with it
            DoMyHotSpotStuff (hotSpotID, &myCustomData);
    }
}
```

Your intercept procedure is called for clicks on any hot spot. You should check to see if it is your type of hot spot and, if so, extract the custom hot spot atom and do whatever is appropriate for your hot spot type (`DoMyHotSpotStuff`).

When you no longer need the intercept procedure you should call `QTVRInstallInterceptProc` again with the same selector and a nil procedure pointer and then call `DisposeRoutineDescriptor` on `myProc`.

Apple reserves all hot spot and atom types with lowercase letters. Your custom hot spot type should contain all uppercase letters.

## See Also

- [Single-node panoramic movies](single-node_panoramic_movies.md)
  Store a QTVR track, a panorama track, and a panorama image track in a single-node panoramic movie.
- [Single-node object movies](single-node_object_movies.md)
  Store a QTVR track, an object track, and an object image track in a single-node object movie.
- [Multinode movies](multinode_movies.md)
  Store any number of object and panoramic nodes in a multinode QuickTime VR movie.
- [Getting the name of a QuickTime VR node](getting_the_name_of_a_quicktime_vr_node.md)
  Retrieve information from a QuickTime VR node with QuickTime atom container functions.
- [Adding atom containers in a QuickTime VR Movie](adding_atom_containers_in_a_quicktime_vr_movie.md)
  Add node information to your QuickTime VR world.
- [Optimizing QuickTime VR movies for web playback](optimizing_quicktime_vr_movies_for_web_playback.md)
  Prevent having to download an entire movie before starting playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/adding_custom_atoms_in_a_quicktime_vr_movie)*