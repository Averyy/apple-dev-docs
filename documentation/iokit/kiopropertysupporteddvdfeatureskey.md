# kIOPropertySupportedDVDFeaturesKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertySupportedDVDFeaturesKey
```

#### Discussion

This key is used to define the supported DVD Features for a particular optical device and it has an associated bitfield. See <IOKit/scsi/IOSCSIMultimediaCommandsDevice.h> for definitions of the bits and associated bitmasks.

Requirement: Mandatory for optical devices (Peripheral Device Type 05h).

Example:

```occ
 
 
<dict>
   <key>Device Characteristics</key>
   <dict>
   	<key>Vendor Name</key>
   	<string>Apple</string>
   	<key>Product Name</key>
   	<string>SuperDrive</string>
   	<key>Product Revision Level</key>
   	<string>1.0</string>
   	<key>CD Features</key>
   	<integer>1663</integer>
   	<key>DVD Features</key>
   	<integer>103</integer>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopropertysupporteddvdfeatureskey)*