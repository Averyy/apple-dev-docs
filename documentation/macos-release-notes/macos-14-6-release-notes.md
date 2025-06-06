# macOS Sonoma 14.6 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 14.5 SDK provides support to develop apps for Mac computers running Sonoma 14.6. The SDK comes bundled with Xcode 15.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.4, see [`Xcode 15.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_4-release-notes).

##### Arkit

###### Resolved Issues

- Fixed: iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when initializing `ARSkeletonDefinition`.  (128038936)

##### Core Spotlight

###### Resolved Issues

- Fixed: iPhone and iPad apps on Apple Silicon Macs quit unexpectedly when invoking `-[CSSearchableItemAttributeSet setActionIdentifiers:]`.  (128039095)

##### Finder

###### Resolved Issues

- Fixed: Home Videos unexpectedly sync as Music Videos to iPod nano (7th generation).  (94899119)

##### Video Subscriber Account

###### Resolved Issues

- Fixed: iPhone and iPad apps on Apple Silicon Macs quit unexpectedly if `VSOpenTVProviderSettingsURLString` is referenced.  (113562872)

##### Video Toolbox

###### Resolved Issues

- Fixed an issue and now on Apple Silicon, if width or height is greater than 4096 columns or rows and content uses 4:2:0 chroma subsampling and 8-bit depth, the hardware decoder driver will reject it and a software decoder will be automatically selected to ensure artifact-free decoding. AVC (H.264) content at level 5.2 or lower can be handled by the hardware decoder. Content that otherwise conforms to level 5.2 but is high frame rate (e.g. 4k at 100 or 120 fps) is labelled level 6, 6.1 or 6.2 and is also handled by hardware. If content is 10-bit, 4:2:2 or 4:4:4, the hardware decoder will be used.  (122448862)

## See Also

- [macOS Sonoma 14.5 Release Notes](macos-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.4 Release Notes](macos-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.3 Release Notes](macos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.2 Release Notes](macos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.1 Release Notes](macos-14_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14 Release Notes](macos-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-14_6-release-notes)*