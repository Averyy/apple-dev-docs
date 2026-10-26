# cursorLoc

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

The location of the cursor hot spot.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOGPoint cursorLoc;
```

## See Also

### Fields
- [cursorSema](./api-1589162-cursorsema.md)
  Semaphore lock for write access to the shared data in this structure.
- [frame](./api-1589173-frame.md)
  The current cursor frame index.
- [cursorShow](./api-1589134-cursorshow.md)
  The cursor is displayed when cursorShow is 0.
- [cursorObscured](./api-1589153-cursorobscured.md)
  If this is true, the cursor has been obscured and cursorShow should not be 0. The cursor will be shown again the next time it is moved.
- [shieldFlag](./api-1589159-shieldflag.md)
  When this is set to true the cursor will not be displayed in the region specified by shieldRect.
- [shielded](./api-1589142-shielded.md)
  True if the cursor has been hidden because it entered the shielded region.
- [saveRect](./api-1589184-saverect.md)
  The region that is saved underneath the cursor in software cursor mode.
- [shieldRect](./api-1589143-shieldrect.md)
  The region that the cursor will not be displayed in if shieldFlag is true.
- [cursorRect](./api-1589191-cursorrect.md)
  The region that the cursor image currently occupies in software cursor mode.
- [oldCursorRect](./api-1589164-oldcursorrect.md)
  The region that the cursor image occupied the last time the cursor was drawn in software cursor mode.
- [screenBounds](./api-1589171-screenbounds.md)
  The region that the current screen occupies.
- [version](./api-1589186-version.md)
  Contains kIOFBCurrentShmemVersion so that a user client can ensure it is using the same version of this structure as the kernel.
- [structSize](./api-1589192-structsize.md)
  Contains the size of this structure.
- [vblTime](./api-1589189-vbltime.md)
  The time of the most recent vertical blanking.
- [vblDelta](./api-1589151-vbldelta.md)
  The interval between the two most recent vertical blankings.
- [vblCount](./api-1589179-vblcount.md)
  A running count of vertical blank interrupts.
- [reservedC](./api-1589141-reservedc.md)
  Reserved for future use.
- [hardwareCursorCapable](./api-1589150-hardwarecursorcapable.md)
  True if the hardware is capable of using hardware cursor mode.
- [hardwareCursorActive](./api-1589174-hardwarecursoractive.md)
  True if currently using the hardware cursor mode.
- [reservedB](./api-1589172-reservedb.md)
  Reserved for future use.
- [cursorSize](./api-1589187-cursorsize.md)
  This array contains the cursor sizes indexed by frame.
- [hotSpot](./api-1589183-hotspot.md)
  This array contains the location of the cursor hot spots indexed by frame. The hot spots coordinates are given relative to the top left corner of the cursor image.
- [cursor](./api-1589137-cursor.md)
  A union of structures that define the cursor images. The structure used depends on the framebuffer's bit depth. These structures are defined above.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/stdfbshmem_t/1589169-cursorloc)*